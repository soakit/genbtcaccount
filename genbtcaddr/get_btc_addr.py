# -*- coding: utf8 -*-

import sys
import ctypes
from ctypes import *
import logging
# import _thread
from multiprocessing import cpu_count
import time

import get_bitcoin as bt
platform = sys.platform
print("platform: " + platform)
if 'darwin' == platform:
    DLL_PATH = "/Users/erkoliu/Documents/workspace/genbtcaccount/getbtc/build/libgenbtcaddr.dylib"
elif ('linux' == platform or 'linux2' == platform):
    DLL_PATH = "../getbtc/build/libgenbtcaddr.so"
else:
    DLL_PATH = "./../x64/Debug/getbtc.dll"

func = cdll.LoadLibrary(DLL_PATH)


def write_file(mnemonic, pri, btc_addr, btc_banlance):
    fo = open("btc.txt", "a+")
    fo.write("mnemonic:" + mnemonic +"pri:"+ pri + "\npub:" + btc_addr + "\nbalance:{}".format(btc_banlance))
    fo.close()

def notification(mnemonic, pri, btc_addr, btc_banlance):
    print("mnemonic: " + mnemonic + "pri: "+pri+"\nbtc_addr: "+btc_addr)
    print("balance:{}".format(btc_banlance))
    
    # 1.写文件通知
    write_file(mnemonic, pri, btc_addr, btc_banlance)

def get_mnemonic(mn_len, mnemonic):
    # val = bytes(mnemonic, encoding='utf-8')
    func.gen_mnemonic(mn_len, mnemonic)
    

def gen_btc_account(mnemonic, passphrase, s):
    func.gen_btc_account(mnemonic, passphrase, s)
    
    
def get_btc_banlance(mnemonic, pri, btc_addr):
    btc_banlance = bt.get_bitcoin_balance(btc_addr)
    if bt.is_zero_balance(btc_banlance):
        notification(mnemonic, pri, btc_addr, btc_banlance)
        return 1
    else:
        print("*******************continue find!*******************")
        return 0

def main_run_btc_(thread_index):
    main_index = 0
    sub_index = 0
    while 1:
        try:
            # 1.生成助记词
            array_type = c_char * 256
            mnemonic_arr = array_type()
            get_mnemonic(12,mnemonic_arr)
            mn_arr = bytearray(mnemonic_arr)
            mnemonic = mn_arr.decode("utf-8").strip(b'\x00'.decode())
            
            # 2.通过助记词生成私钥和地址
            mn_b = bytes(mnemonic)
            passphrase = bytes('')
            print("mn_b:" + mn_b)
            print("passphrase:" + passphrase)
            
            array_pri_type = c_char * 64
            pri = array_pri_type()
            
            array_addr_type = c_char * 64
            addr = array_addr_type()
            
            class accountSturct(Structure):
                _fields_=[('pri',c_char*64),('addr',c_char*64)]
            
            btc_account = accountSturct*3
            
            btc_ac = btc_account()
            gen_btc_account(mn_b, passphrase, btc_ac)
            
            # 3.查询判断是否有余额
            for btc in btc_ac:
                print(btc.pri.decode())
                print(btc.addr.decode())
                get_btc_banlance(mn_b, btc.pri.decode(), btc.addr.decode())

            time.sleep(2.4)
            
        except Exception as err:
            logging.exception(err)
            print("------------error, thread_index:-----------".format(thread_index))
            print(err)

        print("-----thead:{}---{}--{}-----".format(thread_index,main_index, sub_index))
        sub_index = sub_index + 1
        if sub_index >= 1000:
            main_index = main_index + 1
            sub_index = 0

def thread_run():
    main_run_btc_(1)
    # cpu_num = cpu_count()
    # for i in range(cpu_num):
    #     _thread.start_new_thread(main_run_btc_, (i+1,))

if __name__ == "__main__":
    main_index = 0
    sub_index = 0
    thread_run()
    # while 1:
    #     pass

    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
