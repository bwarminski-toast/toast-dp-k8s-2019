import csv
import random
import datetime

def generateRows():
    txId = 0
    for i in range(100):
        txId += 1
        customerId = random.randint(1,100)
        storeId = random.randint(1,10)
        cost = random.randint(10,1000)
        purchaseDateTime = datetime.datetime.now() - datetime.timedelta(days=random.randint(1,365))
        yield (txId, customerId, storeId, cost, purchaseDateTime)

if __name__ == "__main__":
    # transactionId, customerId, storeId, cost, purchaseDateTime
    # customerId rand 1-100
    # storeId rand 1-10
    # createdDate < purchaseDateTime

    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(generateRows())
    # write to file
