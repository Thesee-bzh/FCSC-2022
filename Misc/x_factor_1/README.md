# Misc / X Factor 1

## Challenge :star:
> Un commanditaire vous a demandé de récupérer les données ultra secrètes d'une entreprise concurrente. Vous avez tenté plusieurs approches de recherche de vulnérabilités sur les serveurs exposés qui se sont malheureusement révélées infructueuses : les serveurs de l'entreprise ont l'air solides et bien protégés. L'intrusion physique dans les locaux paraît complexe vu tous les badges d'accès nécessaires et les caméras de surveillance.

> Une possibilité réside dans l'accès distant qu'ont les employés de l'entreprise à leur portail de travail collaboratif : l'accès à celui-ci se fait via deux facteurs d'authentification, un mot de passe ainsi qu'un token physique à brancher sur l'USB avec reconnaissance biométrique d'empreinte digitale. Même en cas de vol de celui-ci, il sera difficile de l'exploiter. Installer un malware evil maid sur un laptop de l'entreprise n'est pas une option : ceux-ci sont très bien protégés avec du secure boot via TPM, et du chiffrement de disque faisant usage du token.

> Mais tout espoir n'est pas perdu ! Vous profitez du voyage en train d'un des employés et de sa fugace absence au wagon bar pour brancher discrètement un sniffer USB miniaturisé sur le laptop. Vous glissez aussi une caméra cachée au dessus de son siège qui n'a pu capturer que quelques secondes. Vous récupérez la caméra et le sniffer furtivement après sa séance de travail : saurez-vous exploiter les données collectées pour mener à bien votre contrat ?

> Pour obtenir le flag de X-Factor 1/2, vous devez vous logguer avec login et mot de passe. Puis avec le deuxième facteur d'authentification pour obtenir le flag pour X-Factor 2/2.

    Note : les fichiers sont les mêmes pour les deux épreuves X-Factor.

## Inputs
- PCAP file [capture_USB.pcapng](capture_USB.pcapng)
- Video file [login_password.mkv](login_password.mkv)

## Solution
Playing the video file esentially shows us the user logging into a website:
- login page: `https://x-factor.france-cybersecurity-challenge.fr/login`
- username: `johndoe@hypersecret`
- password: we see the user typing it, but we can't see the password

Change the Playback speed to play the video at very (very) low speed (I'm using VLC), such that we can see each letter of the password being displayed briefly:
- password: `jesuishypersecretFCSC2022`

So log at `https://x-factor.france-cybersecurity-challenge.fr/login` with creds `(johndoe@hypersecret, jesuishypersecretFCSC2022)`.

Access is granted and we get the flag.

## Flag
FCSC{72b7a93a094c4bb605f252a388ddd89950da3d801ef1c5debd2ca960a17c0603}
