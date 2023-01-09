# Timeseries Model : Air Quality Data in India (2017 - 2022)
Machine learning time series model ini dibuat untuk memenuhi submission project ke 2 pada kelas dicoding : Belajar Pengembangan Machine Learning

### Penjelasan Dataset
Dataset yang digunakan adalah dateset yang berasal dari kaggle [Air Quality Data in India (2017 - 2022)](https://www.kaggle.com/datasets/fedesoriano/air-quality-data-in-india). Dataset ini memiliki 36192 data dengan 6 atribut. Dengan penjelasan atribut :
- Timestamp: Timestamp in the format YYYY-MM-DD HH:MM:SS
- Year: Year of the measure
- Month: Month of the measure
- Day: Day of the measure
- Hour: Hour of the measure
- PM2.5: Fine particulate matter air pollutant level in air

### Penjelasan Model
- Menggunakan LSTM
- 80% training, 20% validation
- Menggunakan model sequential
- Menggunakan learning rate
- MAE < 10% Skala data (23.861)
- Training Mae : 17.7879
- Validation Mae : 10.6123
