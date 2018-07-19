# coding:UTF-8
import math

#シグモイド関数:マイナスの値は0に近くプラスは1に近い0の場合は0.5が出力される関数
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))
#ニューロン:入力された数の合計値なにかで変換してはじき出す
class Neuron:
    input_sum = 0.0
    output = 0.0

    def SetInput(self, inp):
        self.input_sum += inp

    def GetOut(self):
        self.output = sigmoid(self.input_sum)
        return self.output


#ニューラルネットワーク
class NeuralNetwork:
    neuron = Neuron()
    def commit(self, input_data):
        for data in input_data:
            self.neuron.SetInput(data)
        return self.neuron.GetOut()

neural_network = NeuralNetwork()

trial_data = [1 , 2, 3]
print(neural_network.commit(trial_data))