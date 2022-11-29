COMMISSION_PERCENT = .03
NUMBER_OF_SHARES = 2000.0
ORIGINAL_PRICE_PER_SHARE = 40.0
SALE_PRICE_PER_SHARE = 42.75
PURCHASE_PRICE_WITHOUT_COMMISSION = NUMBER_OF_SHARES * ORIGINAL_PRICE_PER_SHARE
PURCHASE_COMMISSION = PURCHASE_PRICE_WITHOUT_COMMISSION * COMMISSION_PERCENT
PURCHASE_PRICE_WITH_COMMISSION = PURCHASE_PRICE_WITHOUT_COMMISSION + PURCHASE_COMMISSION

print("Joe paid $", format(PURCHASE_PRICE_WITH_COMMISSION, '.2f'), ".", sep='')
print("Joe gave $", format(PURCHASE_COMMISSION, '.2f'), " to his broker for the purchase.", sep='')

SALE_PRICE_WITHOUT_COMMISSION = NUMBER_OF_SHARES * SALE_PRICE_PER_SHARE
SALE_COMMISSION = COMMISSION_PERCENT * SALE_PRICE_WITHOUT_COMMISSION
SALE_PRICE_WITH_COMMISSION = SALE_PRICE_WITHOUT_COMMISSION - SALE_COMMISSION

print("Joe made $", format(SALE_PRICE_WITH_COMMISSION, '.2f'), " on the sale.", sep='')
print("Joe's broker made $", format(SALE_COMMISSION, '.2f'), ".", sep='')

PROFIT = SALE_PRICE_WITH_COMMISSION - PURCHASE_PRICE_WITH_COMMISSION
if(PROFIT > 0):
    print("Joe made $", format(PROFIT, '.2f'), sep='')
elif(PROFIT == 0):
    print("Joe didn't make any money.")
else:
    print("Joe lost $", format((PROFIT * -1), '.2f'), sep='')


# Stock Transaction Program

# These are the given variables in the question.
num_share=2000          # Number of shares
per_share_before=40     # Value of each share when he purchased
com_rate=0.03           # Commission rate for stockbroker
per_share_after=42.75   # Value of each share when sells
commission1=per_share_before*num_share*com_rate # Commission when he buys
commission2=per_share_after*num_share*com_rate  # Commission when he sells

print("The amount of money Joe paid for the stock is $", num_share*per_share_before, sep='' )
print("The amount of commission Joe paid his broker when he bought the stock is $", \
      num_share*per_share_before*com_rate, sep='')
print("The amount that Joe sold the stock for is $", num_share*per_share_after, sep='')
print("The amount of commission Joe paid his broker when he sold the stock is $", \
      num_share*per_share_after*com_rate, sep='')
print("Joe made a profit amount of $", \
      ((per_share_after-per_share_before)*2000)-(commission1+commission2))