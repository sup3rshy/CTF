#include <bits/stdc++.h>
using namespace std;
#define __int64 long long
long long state = 0xFEEDF00DDEADBEEFLL;
__int64 gen_rand()
{
  int j; // [rsp+1Ch] [rbp-24h]
  int i; // [rsp+20h] [rbp-20h]
  unsigned int v3; // [rsp+24h] [rbp-1Ch]
  unsigned __int64 v4; // [rsp+28h] [rbp-18h]
  unsigned __int64 v5; // [rsp+30h] [rbp-10h]
  unsigned __int64 v6; // [rsp+38h] [rbp-8h]
  
  v6 = state & 0x1FF;
  v5 = ((unsigned __int64)state >> 9) & 0x7FF;
  v4 = ((unsigned __int64)state >> 20) & 0x1FFF;
  for ( i = 0; i <= 31; ++i )
  {
    for ( j = 0; j <= 30; ++j )
    {
      v6 = ((v6 >> 4) ^ (v6 >> 8)) & 1 | (2 * (v6)) & 0x1FF;
      v5 = ((v5 >> 8)  ^ (v5 >> 10)) & 1 | (2 * (v5 )) & 0x7FF;
      v4 = ((v4 >> 11) ^ (v4 >> 10) ^ (v4 >> 7) ^ (v4 >> 12)) & 1 | (2 * (v4)) & 0x1FFF;
    }
    v3 = (v5 & (v6) | ((~(v6) & v4) & 0xff)) & 1 | 2 * v3;
  }
  state = v6 | (v4 << 20) | (v5 << 9);
  return v3;
}
int v4[12];
int main() {
    v4[0] = 0x906f6020;
    v4[1] = 0xf38f77ae;
    v4[2] = 0x5ea509fc;
    v4[3] = 0x51396bdd;
    v4[4] = 0x5e6efddf;
    v4[5] = 0x858860a8;
    v4[6] = 0x5295d7bc;
    v4[7] = 0xf382e975;
    v4[8] = 0x9504a2b7;
    v4[9] = 0x675c0e4a;
    v4[10] = 0xbf138153;
    v4[11] = 0xc1706134;
    for (int i = 0; i < 12; i++) {
        int v5 = gen_rand();
        state = ((unsigned int)v4[i] ^ (unsigned __int64)state);
        v4[i] ^= v5;
        printf("0x%x\n", v4[i]);
    }
    return 0;
}
