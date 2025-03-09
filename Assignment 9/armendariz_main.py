import numpy as np
import matplotlib.pyplot as plt

#Generates Different Probability Distributions
class Distributions:
    #Attributes: Distribution - string - Normal, Lognormal, and Laplace, Mean - float, STD - float - Standard Deviation, Size - int - Number of Samples
    def __init__(self, dist: str, mean: float, std: float, size: int):
        self.distribution = dist.lower()
        self.mean = mean
        self.std = std
        self.size = size
        self.data = None
        self.generate_distribution()

    #Returns a String Representation Of The Details
    def __str__(self):
        return f"Distribution: {self.distribution}, Mean: {self.mean}, Std: {self.std}, Size: {self.size}"

    #Generates Distribution Based On Type
    def generate_distribution(self):
        if self.distribution == "normal":
            self.data = np.random.normal(self.mean, self.std, self.size)
        elif self.distribution == "lognormal":
            self.data = np.random.lognormal(self.mean, self.std, self.size)
        elif self.distribution == "laplace":
            self.data = np.random.laplace(self.mean, self.std, self.size)
        else:
            raise ValueError("Invalid Distribution Type. Select: 'normal', 'lognormal', or 'laplace'.")

    #Returns Data
    def get_data(self):
        return self.data

#Generates Probability Using Numpy
class NumpyDistribution:
    #Attributes: Distribution - string - Normal, Lognormal, and Laplace, Mean - float, STD - float - Standard Deviation, Size - int - Number of Samples
    def __init__(self, dist: str, mean: float, std: float, size: int):
        self.distribution = dist.lower()
        self.mean = mean
        self.std = std
        self.size = size
        self.data = None
        self.generate_distribution()

    #Returns a String Representation Of The Details
    def __str__(self):
        return f"Distribution: {self.distribution}, Mean: {self.mean}, Std: {self.std}, Size: {self.size}"

    #Generates Distribution Using Numpy
    def generate_distribution(self):
        dist_methods = {
            "normal": np.random.normal,
            "lognormal": np.random.lognormal,
            "laplace": np.random.laplace
        }
        if self.distribution not in dist_methods:
            raise ValueError("Invalid Distribution Type. Select: 'normal', 'lognormal', or 'laplace'.")

        self.data = dist_methods[self.distribution](self.mean, self.std, self.size)

    #Returns Generated Distribution Data
    def get_data(self):
        return self.data

#Plots Sine and Cosine Functions
def plot_trig_functions():
    x = np.linspace(0, 2 * np.pi, 1000)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    #Plots On The Same Axes
    plt.figure()
    plt.plot(x, y_sin, label="sin(x)")
    plt.plot(x, y_cos, label="cos(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Sine And Cosine On The Same Axes")
    plt.legend()
    plt.grid()
    plt.show()

    #Plots Sharing The Y
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(x, y_sin, 'g-', label="sin(x)")
    ax2.plot(x, y_cos, 'b-', label="cos(x)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("sin(x)", color='g')
    ax2.set_ylabel("cos(x)", color='b')
    plt.title("Sine And Cosine On Shared Y-Axis")
    plt.grid()
    plt.show()

    #Plots Sharing The X
    fig, axs = plt.subplots(2, 1, sharex=True)
    axs[0].plot(x, y_sin, 'r-', label="sin(x)")
    axs[0].set_ylabel("sin(x)")
    axs[0].grid()
    axs[0].legend()
    axs[1].plot(x, y_cos, 'b-', label="cos(x)")
    axs[1].set_ylabel("cos(x)")
    axs[1].grid()
    axs[1].legend()
    plt.xlabel("x")
    plt.suptitle("Sine And Cosine On Shared X-Axis)")
    plt.show()


if __name__ == "__main__":
    normal_dist = Distributions("normal", 0, 1, 1000)
    lognormal_dist = NumpyDistribution("lognormal", 1, 0.5, 1000)
    plot_trig_functions()
