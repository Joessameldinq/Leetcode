class Fancy{
    const long long MOD = 1e9 + 7;
    vector<long long> seq;
    long long mul = 1, add = 0;

    long long pow(long long base,long long exp){
        long long res = 1;
        base %= MOD;
        while(exp > 0){
            if(exp & 1) res = res * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return res;
    }
    long long modInv(long long x){
        return pow(x,MOD-2);
    }
public:
    Fancy(){}
    void append(int val){
        long long stored = (val - add % MOD + MOD) % MOD * modInv(mul) % MOD;
        seq.push_back(stored);
    }

    void addAll(int inc){
        add = (add + inc) % MOD;
    }
    void multAll(int m){
        mul = (mul * m) % MOD;
        add = (add * m) % MOD;

    }
    int getIndex(int idx){
        if(idx >= (int)seq.size())return -1;
        return (seq[idx] * mul % MOD + add) % MOD;
    }
};