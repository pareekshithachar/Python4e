text = "X-DSPAM-Confidence:    0.8475";
r=text.find('0')
p=text[r:]
q=float(p)
print(q)
