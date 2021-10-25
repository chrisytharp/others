import panda as pd

df = pd.read_excel("results.csv")

deviceName = df['DeviceName']

print(deviceName)
