# SicurezzaDelleAppMod1_2026

Tool di supporto per il corso di Sicurezza delle Applicazioni - Modulo 1 presso il DISEGIM UniParthenope a Nola

## Descrizione

Questo repository contiene materiali didattici, esempi di codice e risorse utili per gli studenti che seguono il corso di Sicurezza delle Applicazioni - Modulo 1.

## Uso

Gli studenti possono utilizzare la macchina virttuale fornita per esercitarsi con le tecniche di sicurezza delle applicazioni. Si consiglia di seguire le lezioni e utilizzare i materiali presenti in questo repository per approfondire le conoscenze acquisite.

**La prima volta** che si utilizza il container, è necessario clonare il repository:

```bash
git clone https://github.com/SicurezzaAppDisegimUniparthenope/SicurezzaDelleAppMod1_2026.git
cd SicurezzaDelleAppMod1_2026
docker compose up -d
```

**Le volte successive**, per aggiornare il repository ed eseguire il container, eseguire i seguenti comandi:

```bash
cd SicurezzaDelleAppMod1_2026
git pull
docker compose up -d
```

La macchina è raggiungibile tramite ssh alla porta 2222 del localhost.

```bash
ssh -p 2222 user@localhost
```

Per accedere alla macchina virtuale, utilizzare le seguenti credenziali:

- Username: `user`
- Password: `user`

L'utente con permessi di amministrazione è toor:

- Username: `toor`
- Password: `toor`

## Sorgenti

I sorgenti del container Docker sono disponibili nel progetto [Builder del progetto Sicurezza delle Applicazioni - Modulo 1 - 2026](https://github.com/SicurezzaAppDisegimUniparthenope/SicurezzaDelleAppMod1_2026_builder)