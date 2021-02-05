import csv, pandas as pd, flexpoolapi as fp

#conversion from wei to eth
eth = .000000000000000001

#conversion from hash/s to megahash/s
hash = .000001

#declare your worker
miner = fp.miner("INSERT WALLET ADDRESS OF WORKER HERE")

#eth balance
mb = miner.balance()*eth

#effective hashrate in mgh/s
hr = miner.daily_average_stats().effective_hashrate*hash

#estimated daily revenue in eth
mdr = miner.estimated_daily_revenue()*eth

#valid shares
vshares = miner.daily_average_stats().valid_shares

#stale shares
sshares = miner.daily_average_stats().stale_shares

#invalid shares
ishares = miner.daily_average_stats().invalid_shares

#pool luck % and roundtime in minutes
luck, rt = fp.pool.avg_luck_roundtime()

#worker round share % per block
rshare = miner.round_share()*100

#total donated to pool in eth
donate = miner.total_donated()*eth

#lifetime earnings in eth
total = miner.total_paid()*eth


list = [mb, hr, mdr, vshares, sshares, ishares, luck*100, rt/60, rshare, donate, total]


#BEGIN ONLY NEEDED FOR INITIAL CSV FILE
def getinfo():
    df = pd.DataFrame(columns=['Balance', 'Average Hashrate', 'Est Daily Revenue', 'Valid Shares',
                               'Stale Shares', 'Invalid Shares', '% Average Pool Luck', 'Average Pool Round Time (min)',
                               '% Round Share', 'Total Donated', 'Lifetime Earnings'])
    new_row = pd.Series({'Balance': mb, 'Average Hashrate': hr, 'Est Daily Revenue': mdr, 'Valid Shares': vshares,
                         'Stale Shares': sshares, 'Invalid Shares': ishares, '% Average Pool Luck': luck,
                         'Average Pool Round Time (min)': rt, '% Round Share': rshare, 'Total Donated': donate,
                         'Lifetime Earnings': total})
#END

for i in range(1):
      #only need fields for initial csv file
    # fields = ['Balance', 'Average Hashrate', 'Est Daily Revenue', 'Valid Shares', 'Stale Shares',
    #               'Invalid Shares', '% Average Pool Luck', 'Average Pool Round Time (min)', '% Round Share',
    #               'Total Donated', 'Lifetime Earnings']
    with open('flexpoolmining.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        
        #only need writerow fields for initial csv file
        # writer.writerow(fields)
        
        writer.writerow(list)
