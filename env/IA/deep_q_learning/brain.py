from keras.layers import Input, Dense, Dropout
from keras.models import Model
from keras.optimizers import Adam

class Brain(object):
    def __init__(self, learnig_rate = 0.001, number_actions = 5):
        self.learnig_rate = learnig_rate

        # CRIAÇÃO DA CAMADA DE ENTRADA COMPOSTA PELO INPUT STATE
        states = Input(shape = (3,))

        # CRIAÇÃO DAS CAMADAS OCULTAS DA REDE NEURAL DENSA
        x = Dense(units=64, activation='sigmoid')(states)
        x = Dropout(rate = 0.1)(x)
        y = Dense(units=32, activation='sigmoid')(x)
        y = Dropout(rate = 0.1)(y)

        # CRIAÇÃO DA CAMADA DE SAÍDA, CONECTA COM A ÚLTIMA CAMADA OCULTA
        q_values = Dense(units=number_actions, activation = 'softmax')(y)

        # AGREGAR TODAS AS CAMADAS EM UM MODELO (OBJETO MODEL)
        self.model = Model(inputs = states, outputs = q_values)

        # COMPILAÇÃO DO MODELO, UTILIZADO FUNÇÃO DE ERRO E OTIMIZAÇÃO
        self.model.compile(loss = 'mse', optimizer = Adam(learning_rate = self.learnig_rate))