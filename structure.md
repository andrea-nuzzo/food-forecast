```
food forecast/
│
├── data/               # Cartella per dati grezzi e trasformati
│   ├── raw/            # Dati non modificati, es. CSV o Excel scaricati
│   └── processed/      # Dati trasformati pronti per l'ingestione o ML
│
├── notebooks/          # Jupyter notebooks per l'esplorazione dei dati
│
├── src/                # Codice sorgente del progetto
│   ├── fetch/          # Moduli per il recupero dei dati
│   ├── transform/      # Moduli per la trasformazione dei dati
│   ├── ingest/         # Moduli per l'ingestione dei dati nel database
│   └── ml/             # Codice relativo a MLflow e reti neurali
│
├── tests/              # Test unitari e di integrazione
│
├── scripts/            # Script utili, es. avvio di training o setup
│
└── pyproject.toml      # Configurazione di Poetry e dipendenze del progetto
```