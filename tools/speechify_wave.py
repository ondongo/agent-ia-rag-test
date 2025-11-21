import aiohttp
import os
import asyncio

async def generate_single_wave(session, access_token, content_chunk, is_first_chunk=False, is_last_chunk=False):
    """
    Génère un wave audio pour un chunk de texte
    """
    SPEECH_GEN_URL = "https://api.sws.speechify.com/v1/audio/speech"
    VOICE_ID = "3448f188-b84b-4242-a905-d6e0a203b941" # À remplacer par la voix choisie

    # Construction du texte avec préfixe et suffixe conditionnels
    text_parts = []
    if is_first_chunk:
        text_parts.append("Cher compatriote,")
    text_parts.append(content_chunk)
    if is_last_chunk:
        text_parts.append("Vive la République et Vive la France.")

    final_text = " ".join(text_parts)

    speech_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "input": final_text,
        "voice_id": VOICE_ID,
        "language": "fr-FR",
        "model": "simba-multilingual",
        "options": {
            "text_normalization": True,
            "loudness_normalization": False
        }
    }

    async with session.post(SPEECH_GEN_URL, headers=speech_headers, json=payload) as speech_response:
        response_data = await speech_response.json()
        return response_data.get("audio_data")

async def speechify_wave(content: str) -> list:
    """
    Génère des data audio waves avec l'API Speechify
    """
    try:
        SPEECHIFY_API_KEY = os.getenv("SPEECHIFY_API_KEY")
        AUTH_TOKEN_URL = "https://api.sws.speechify.com/v1/auth/token"

        async with aiohttp.ClientSession() as session:
            # Authentification
            auth_headers = {
                "Authorization": f"Bearer {SPEECHIFY_API_KEY}",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            auth_data = "grant_type=client_credentials&scope=audio:speech"

            async with session.post(AUTH_TOKEN_URL, headers=auth_headers, data=auth_data) as auth_response:
                auth_json = await auth_response.json()
                access_token = auth_json.get("access_token")

            # Nettoyage du contenu
            cleaned_content = str(content).replace('<br/>', '\n').replace('<strong>', '').replace('</strong>', '')

            # Calcul du nombre de caractères et division en chunks
            total_chars = len(cleaned_content)
            max_chars_per_chunk = 1900

            # Génération des waves pour chaque chunk
            waves = []
            current_idx = 0
            chunk_number = 0

            while current_idx < total_chars:
                # Calcul de l'index de fin potentiel
                end_idx = min(current_idx + max_chars_per_chunk, total_chars)

                # Si on n'est pas à la fin du texte, on cherche le dernier espace
                if end_idx < total_chars:
                    # On cherche le dernier espace dans les 100 derniers caractères pour éviter de trop reculer
                    last_space = cleaned_content.rfind(' ', current_idx, end_idx)
                    if last_space != -1:
                        end_idx = last_space + 1  # +1 pour inclure l'espace

                chunk = cleaned_content[current_idx:end_idx].strip()
                if chunk:  # On ne traite que les chunks non vides
                    wave_data = await generate_single_wave(
                        session,
                        access_token,
                        chunk,
                        is_first_chunk=(chunk_number == 0),
                        is_last_chunk=(end_idx >= total_chars)
                    )
                    if wave_data:
                        waves.append(wave_data)

                current_idx = end_idx
                chunk_number += 1

            return waves

    except Exception as e:
        print(str(e))
        return []

if __name__ == "__main__":
    asyncio.run(speechify_wave())
