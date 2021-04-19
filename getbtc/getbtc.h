#pragma once

#define EXPORTFUC (extern "C" __declspec(dllexport))

#define CODE_FAILSE			0
#define CODE_SUCCESS		1


typedef enum {
	TYPE_1 = 0,			// 1��ַ����
	TYPE_3 = 1,			// 3��ַ��ͨ
	TYPE_bc = 2,		// bc��ַ��ͨ
	TYPE_LAST = 3		// 

}TYPE;

typedef struct btc_account 
{
	char pri[64];		// wif��ʽ
	char addr[64];		// ��ַ
}btc_account;

// 44
#define VERSION_XPUBLIC  0x0488b21e  // xpub
#define VERSION_XPRIVATE 0x0488ade4  // xprv

// 49
#define VERSION_BIP49_XPUBLIC  0x049d7cb2  // xpub
#define VERSION_BIP49_XPRIVATE 0x049d7878  // xprv

// 84
#define VERSION_BIP84_XPUBLIC  0x04b24746  // xpub
#define VERSION_BIP84_XPRIVATE 0x04b2430c  // xprv

// �������Ǵ�
__declspec(dllexport)
int gen_mnemonic(int len, char* mnemonic);


// int gen_btc_account(const char* mnemonic, const char* passphrase, char* pri, char* address);
__declspec(dllexport)
int gen_btc_account(const char* mnemonic, const char* passphrase, btc_account* accoun);

__declspec(dllexport)
int test_call(int a);
