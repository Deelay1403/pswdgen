# pswdgen 0.1v
A program created for generating human-friendly passwords combined with words and special characters

## Requirements

- Linux/MacOS/Windows

## Usage 

Run in terminal using python e.g. _**python pswdgen.py**_

Could be added as an alias:

`sudo cp pswdgen.py /usr/local/bin/pswdgen`<br />
`sudo chmod +x /usr/local/bin/pswdgen`<br />
`alias pswdgen="python /usr/local/bin/pswdgen"`<br />

    params:
    -c, --count: How many passwords should be generated
    -w, --words: How many words password should contain
    -n, --numbers: How many numbers should be in password
    -s, --specialchars: How many special characters should be in password
    -f, --file: File name to save output
    -h: Help

## Example output
<pre>
python.exe .\pswdgen.py -c 10 -w 3

0: ['GruboskornyWielomilionowyCiezarny#72']
1: ['WypelzywacNiehonorowyCenny01$']
2: ['OblednyJakiAntenowy8&5']
3: ['RozromansowacWysmakowywacPodaniowy39%']
4: ['BarykadowacZamanifestowacPrzemocny65&']
5: ['MajaUzasadnionyAdaptacyjny+42']
6: ['PrzemacerowacPosforowacKapitalochlonny^27']
7: ['WylakierowacSkompromitowacBlyskowy&03']
8: ['ZywicowacSzarfowacRecesywny&55']
9: ['SpostponowacOdowocowacFutrzany+32']

</pre>