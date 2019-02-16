data2016all = table2array(x2016all).';
all16in = data2016all(2:19,:);
all16result = NetworkB(all16in);

data2016part = table2array(x2016partial).';
part16in = data2016part(2:13,:);
part16result = NetworkA(part16in);

data2017all = table2array(x2017all).';
all17in = data2017all(2:19,:);
all17result = NetworkB(all17in);

data2017part = table2array(x2017partial).';
part17in = data2017part(2:13,:);
part17result = NetworkA(part17in);