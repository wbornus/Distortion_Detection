import eval_utils

if __name__ == '__main__':
    directory = './eval_samples/masna_piosenka_mod.wav'
    eval_utils.predict_and_visualize(directory, frame_length=0.100)