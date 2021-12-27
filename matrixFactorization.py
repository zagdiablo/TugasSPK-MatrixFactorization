import pandas as pd


"""
Nama:   Adhitia Nugraha
NIM:    181011401667
Kelas:  07TPLM008

Tugas untuk mendapatkan nilai UAS
(Nim 2, 7)Buatlah project menggunakan matrix factorization

berikut adalah program rekomendasi film menggunakan matrix factorization
"""


def main():
    # membaca dan mengambil data dari file u.data
    column_names = ['user_id', 'item_id', 'rating', 'timestamp']
    df = pd.read_csv('u.data', sep='\t', names = column_names)

    # membuat dataframe dan mengurutkan data dengan patokan judul film
    # lalu menggabungkan dataframe
    movie_titles = pd.read_csv('Movie_Id_Titles')
    df = pd.merge(df, movie_titles, on='item_id')

    # membuat dataframe berdasarkan rating
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())

    # pivot table rating berdasarkan user_id
    moviemat = df.pivot_table(index='user_id', columns='title', values='rating')

    # mengambil salah satu judul film dari pivot table untuk dicari rekomendasinya
    base_movie = moviemat['Star Wars (1977)'] # << ganti judul film untuk menampilkan rekomendasi lain

    # mencari data film yang mirip menggunakan korelasi dari variabel judul film base_movie
    similar_to_base_movie = moviemat.corrwith(base_movie)
    corr_movie = pd.DataFrame(similar_to_base_movie, columns=['Correlation'])
    # membuang data yg berisikan NaN
    corr_movie.dropna(inplace=True)
    # menggabungkan data rating ke dataframe film yg mirip
    corr_movie = corr_movie.join(ratings['num of ratings'])

    # menampilkan data film rekomedasi berdasarkan variabel base_movie yg dimana 
    # jumlah rating yang telah diberikan oleh user harus lebih dari 100
    print(corr_movie[corr_movie['num of ratings']>100].sort_values('Correlation', ascending=False).head())


if __name__ == "__main__":
    main()