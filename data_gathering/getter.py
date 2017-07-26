import argparse
import urllib2
import os
import thread
import time
'''
Easy addintion to more sources.
'''
SOURCES ={
    'CAPTCHAS' : 'https://projecteuler.net/captcha/show_captcha.php'
}


def startDownloads(toget, ranges, thread_id):
    '''
    Downloads files.

    :param      toget: What is it going to be downladed. This is used to get the
                       link.
    :param      quantity: How many downloads to perform

    '''
    for x in range(ranges[0], ranges[1]):
        with open('{}/{}.png'.format(toget,x), 'w' ) as file:
            file.write(urllib2.urlopen(SOURCES[toget], timeout = 5).read())




def preDownloadCheck(toget, quantity, threads):
    '''
    Checks that the provided arguments are valid for download. If missing directory
    then it creates one.

    :param      toget: What is it going to be downladed. This is used to get the
                       link.
    :param      quantity: How many downloads to perform

    :param      threads: number of threads to run at the same time.
    '''
    if not quantity.isdigit() and int(quantity) > 0:
        print ('Please provide a valid quantity. n > 0')
    quantity = int(quantity)
    if toget not in SOURCES:
        print ('There are no sources for {}. Exiting.'.format(toget))
        exit()
    if not 4 >= int(threads) >= 1:
        print('Please insert a valid thread number 1<= thread <=3')
    threads = int(threads)
    if not os.path.exists(toget):
        os.makedirs(toget)

    increasigJobs = quantity/ threads
    ranges = [0, increasigJobs]

    for numThread in range(threads):
        print ranges
        thread.start_new_thread(startDownloads, (toget, ranges, numThread))
        ranges = [ranges[1], ranges[1]+increasigJobs]

    # This might not be the best solution.
    path, dirs, files = os.walk(toget).next()
    while not len(files) >= quantity:
        print 'Waiting... {} out of {}'.format(len(files), quantity)
        path, dirs, files = os.walk(toget).next()
        time.sleep(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    parser.add_argument('--version', action='version', version='0.0.1')

    toGetParser = subparsers.add_parser('get')
    toGetParser.add_argument('toget', help='What to download. Currently only captchas supported. (Ex. getter.py get CAPTCHAS)')
    toGetParser.add_argument('quantity', help='Quantity of CAPTCHAS to download. (Ex. getter.py get CAPTCHAS 100)')
    toGetParser.add_argument('threads', help='Number of threads running at the same time. (Ex. getter.py get CAPTCHAS 100 4)')
    toGetParser.set_defaults(func = lambda args: \
        preDownloadCheck(args.toget, args.quantity, args.threads))
    args = parser.parse_args()
    if 'func' in vars(args):
        args.func(args)
