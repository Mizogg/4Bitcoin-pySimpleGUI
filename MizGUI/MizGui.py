#!/usr/bin/env python
import secp256k1 as ice
import random
import datetime
import os
import webbrowser
import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
from os import path
from bloomfilter import BloomFilter
start_time = datetime.datetime.now()

lines = '=' * 70

information = ('''
https://en.wikipedia.org/wiki/Bitcoin

Bitcoin (Abbreviation: BTC; sign: ₿) is a decentralized digital currency that can be transferred on the peer-to-peer bitcoin network.Bitcoin transactions are verified by network nodes through cryptography and recorded in a public distributed ledger called a blockchain. The cryptocurrency was invented in 2008 by an unknown person or group of people using the name Satoshi Nakamoto.The currency began use in 2009, when its implementation was released as open-source software.
''')
information1 = ('''
https://en.wikipedia.org/wiki/Bitcoin

Bitcoin has been described as an economic bubble by at least eight Nobel Memorial Prize in Economic Sciences recipients.
''')
information2 = ('''
https://en.wikipedia.org/wiki/Bitcoin

The word bitcoin was defined in a white paper published on 31 October 2008. It is a compound of the words bit and coin. No uniform convention for bitcoin capitalization exists; some sources use Bitcoin, capitalized, to refer to the technology and network and bitcoin, lowercase, for the unit of account. The Wall Street Journal, The Chronicle of Higher Education, and the Oxford English Dictionary advocate the use of lowercase bitcoin in all cases.
''')
information3 = ('''
https://en.wikipedia.org/wiki/Bitcoin

The legality of bitcoin varies by region. Nine countries have fully banned bitcoin use, while a further fifteen have implicitly banned it. A few governments have used bitcoin in some capacity. El Salvador has adopted Bitcoin as legal tender, although use by merchants remains low. Ukraine has accepted cryptocurrency donations to fund the resistance to the 2022 Russian invasion. Iran has used bitcoin to bypass sanctions.
''')
information4 = ('''
https://en.wikipedia.org/wiki/Bitcoin

The unit of account of the bitcoin system is the bitcoin. Currency codes for representing bitcoin are BTC and XBT.
Its Unicode character is ₿. One bitcoin is divisible to eight decimal places. 
Units for smaller amounts of bitcoin are the millibitcoin (mBTC), equal to 1⁄1000 bitcoin, and the satoshi (sat), which is the smallest possible division, and named in homage to bitcoin's creator, representing 1⁄100000000 (one hundred millionth) bitcoin. 100,000 satoshis are one mBTC.
''')
startinfo = (information, information1, information2, information3, information4)
start_time = datetime.datetime.now()


SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme()}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-'}

def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window


def load_addresses(filename):
    global addresses, bloom_filterbtc
    print(f'\n Creating database from \'{filename}\' ...Please Wait...')
    with open(filename, 'rb') as fp:
        bloom_filterbtc = BloomFilter.load(fp)

def create_main_window(settings):
    addr_count = len(bloom_filterbtc)
    sg.theme(settings['theme'])

    menu_def = [['&Menu', ['&Settings', '&Exit']], ['&About', ['&MizoggHome', '&MizoggPython']]]

    layout = [[sg.Menu(menu_def)],
              [sg.Text('Made by mizogg.co.uk ', size=(19,1), font=('Comic sans ms', 13)), sg.Text('This program has been running for............', size=(30,1), font=('Comic sans ms', 11)), sg.Text('', size=(12,1), font=('Comic sans ms', 11), key='_DATE_')],
              [sg.Text(' ')],
              [sg.Output(size=(100, 18), font=('Comic sans ms', 10), key='out')],
              [sg.Text('Start Range IN BITS -> ', size=(22,1), font=('Comic sans ms', 12)),
               sg.Input('1', size=(12,1), key='bitx', background_color='green', text_color='white', font=('Comic sans ms', 11))],
               [sg.Text('Stop Range IN BITS -> ', size=(22,1), font=('Comic sans ms', 12)),
               sg.Input('256', size=(12,1), key='bity', background_color='red', text_color='white', font=('Comic sans ms', 11))],
              [sg.Button('Start/Stop',  font=('Comic sans ms', 10)), sg.Text('Total Addresses Looking for From File : ', size=(35,1), font=('Comic sans ms', 14)), sg.Text(addr_count, font=('Comic sans ms', 16)), sg.Text('', size=(10,1))]]

    return sg.Window('MIZOGG Fullbitgui.py',
                     layout=layout,
                     default_element_size=(10,1))


def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    generator = False
    load_addresses('puzzle.bf')
    addr_count = len(bloom_filterbtc)
    while True:
        if window is None:
            window = create_main_window(settings)
        event, values = window.Read(timeout=10)
        window.Element('_DATE_').Update(str(datetime.datetime.now()-start_time))
        if event in (None, 'Exit'):
            break
        elif event == 'Start/Stop':
            print(random.choice(startinfo))
            generator = not generator
            count=0
            total=0
            found=0

        if generator:
            x=int(values['bitx'])
            y=int(values['bity'])
            dec= random.randrange(2**x,2**y)
            HEX = "%064x" % dec
            caddr = ice.privatekey_to_address(0, True, dec)
            uaddr = ice.privatekey_to_address(0, False, dec)
            p2sh = ice.privatekey_to_address(1, True, dec)
            bech32 = ice.privatekey_to_address(2, True, dec)
            length = len(bin(dec))
            length -= 2
            if caddr in bloom_filterbtc:
                found += 1
                output = f'''\n
{lines}
  : Private Key DEC : {dec} Bits : {length}
{lines}
  : Private Key HEX : {HEX}
{lines}
  : BTC Address Compressed : {caddr}
{lines}
'''
                print(output)
                with open('foundcaddr.txt', 'a', encoding='utf-8') as f:
                    f.write(output)

            if uaddr in bloom_filterbtc:
                found += 1
                output = f'''\n
{lines}
  : Private Key DEC : {dec} Bits : {length}
{lines}
  : Private Key HEX : {HEX}
{lines}
  : BTC Address Uncompressed : {uaddr}
{lines}
'''
                print(output)
                with open('founduaddr.txt', 'a', encoding='utf-8') as f:
                    f.write(output)

            if p2sh in bloom_filterbtc:
                found += 1
                output = f'''\n
{lines}
  : Private Key DEC : {dec} Bits : {length}
{lines}
  : Private Key HEX : {HEX}
{lines}
  : BTC Address Segwit : {p2sh}
{lines}
'''
                print(output)
                with open('foundp2sh.txt', 'a', encoding='utf-8') as f:
                    f.write(output)

            if bech32 in bloom_filterbtc:
                found += 1
                output = f'''\n
{lines}
  : Private Key DEC : {dec} Bits : {length}
{lines}
  : Private Key HEX : {HEX}
{lines}
  : BTC Address Bc1 : {bech32}
{lines}
'''
                print(output)
                with open('foundbech32.txt', 'a', encoding='utf-8') as f:
                    f.write(output)
                    
            else:
                running = f'''\nFound [{found}]
Scan Num = [{count}] Total Addresses [{total}]
{lines}
  : Private Key DEC : {dec} Bits : {length}
{lines}
  : Private Key HEX : {HEX}
{lines}
  : BTC Address Compressed : {caddr}
{lines}
  : BTC Address Uncompressed : {uaddr}
{lines}
  : BTC Address Segwit : {p2sh}
{lines}
  : BTC Address Bc1 : {bech32}
{lines}
'''
                print(running)
            count+=1
            total+=4

            
        elif event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)


        elif event == 'MizoggHome':
            webbrowser.open_new_tab("https://mizogg.co.uk")
        
        elif event == 'MizoggPython':
            webbrowser.open_new_tab("https://mizogg.com")

    
    window.Close()

if __name__ == '__main__':  
    addresses = list()
    bloom_filterbtc = set()
    main()
