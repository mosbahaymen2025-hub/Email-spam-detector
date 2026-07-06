audio_data=[[0.5,1],[1.0,2],[4.0,8]]
mystery_audio = [1.2, 1.5]


def calculate_distance(vector1, vector2):
    total_sum = 0
    for i in range(len(vector1)):
        total_sum = total_sum + (vector1[i] - vector2[i]) ** 2
    return (total_sum ** 0.5)


def closest(mystery_audio,audio_data):
    min_dis = 10000
    dis = 0
    best_index = 0
    for i in range(len(audio_data)):
        dis = calculate_distance(mystery_audio,audio_data[i])
        if min_dis > dis :
            min_dis = dis
            best_index = i
    return best_index

print (closest (mystery_audio,audio_data))
