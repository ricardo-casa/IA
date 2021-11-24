import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def k_means(k, data):
    """
    https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/
    para la implementacion del algoritmo de k means se deben seguir los siguientes pasos: 
    
    1) Elejir el numero de clusteres o conglomerados (k), recomendable escojerlos entre mas lejania entre ellos 
    2) se deben elejir k puntos aleatorios como medias iniciales 
    3) Asignar todos los puntos al cluster mas cercano (la media inicial mas cercana)
    4) Volver a calcular el centroide de el cluster formado 
    5) Repetir pasos 3 y 4 hasta que ya no haya cambios en los centroides.
    """

    # escojer centroides
    centroids = data.sample(n=k)
    difference = 1
    j = 0

    while difference != 0:
        data_aux = data
        i = 1

        for index1, row_centroids in centroids.iterrows():
            distances = []
            for index2, row_data in data_aux.iterrows():
                d1 = (row_centroids['x'] - row_data['x']) ** 2
                d2 = (row_centroids['y'] - row_data['y']) ** 2
                distances.append(np.sqrt(d1 + d2))
            data[i] = distances
            i += 1

        column_distance = []
        for index, row in data.iterrows():
            min_distance = row[1]
            pos = 1
            for i in range(k):
                if row[i + 1] < min_distance:
                    min_distance = row[i + 1]
                    pos = i + 1
            column_distance.append(pos)

        data['cluster'] = column_distance
        new_centroids = data.groupby(["cluster"]).mean()[['y', 'x']]

        if j == 0:
            j = j + 1

        difference = (new_centroids['y'] - centroids['y']).sum() + \
                     (new_centroids['x'] - centroids['x']).sum()
        print(difference.sum())
        centroids = data.groupby(["cluster"]).mean()[["y", "x"]]

    for m in range(k):
        data = data[data['cluster'] == m + 1]
        plt.scatter(data['x'], data["y"], c='cyan')

    plt.scatter(centroids['x'], centroids['y'], c='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def perceptron():
    pass


# Press the green button in the gutter to run the script.

# [8, 10], [3, 10.5], [7, 13.5], [5, 18], [5, 13], [6, 9], [9, 11], [3, 18], [8.5, 12], [8, 16]
if __name__ == '__main__':
    vectors = {'x': [8, 3, 7, 5, 5, 6, 9, 3, 8.5, 8, 12, 5], 'y': [10, 10.5, 13.5, 18, 13, 9, 11, 18, 12, 16, 11, 14]}
    km_data = pd.DataFrame(data=vectors)
    k_means(2, km_data)
