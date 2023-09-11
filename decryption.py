inp = 'Oyq, xocfq xtt, hyn ay nf gsyn chxc cny xsa cny dxgf oyjq? Yq chxc chf oyqpf yo vqxzwce nyqgl? Yq chxc chf rxlc wl jsphxsvfxmtf? Wo mych chf rxlc xsa chf fucfqsxt nyqta fuwlc yste ws chf dwsa, xsa wo chf dwsa wclfto wl pyscqyttxmtf – nhxc chfs? PLfP{chfqf_wl_vqxpf_ws_leddfcqe}'
inp = inp.lower()

print(inp)
decryption = {}

s = 'qwertyuiopasdfghjklzxcvbnm, {}_?-–'
for i in s:
    decryption[i] = i

decryption['p'] = 'c'
decryption['l'] = 's'
decryption['f'] = 'e'
decryption['c'] = 't'
decryption['x'] = 'a'
decryption['s'] = 'n'
decryption['n'] = 'w'
decryption['y'] = 'o'
decryption['q'] = 's'
decryption['a'] = 'd'
decryption['g'] = 'k'
decryption['r'] = 'm'
decryption['m'] = 'w'
decryption['w'] = 'o'
decryption['o'] = 'r'

ret = ''
for i in range(len(inp)):
    ret += decryption[inp[i]]

print(ret)