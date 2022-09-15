##endif



## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_

## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/modes.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/nbtheory.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/osrng.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/dh.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/dh2.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/cast.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/rc6.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/mars.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/serpent.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/twofish.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/blowfish.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/camellia.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/des.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/idea.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/rc5.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/seed.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/shacal2.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/skipjack.h>
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/tea.h>
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _WIN32
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/cryptoppLibLink.h>
##endif

from CryptoPP import *

import math

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if _IMPROVED_PACKET_ENCRYPTION_
## Laniatus Games Studio Inc. | WARNING: The following #include directive was ignored:
##include <cryptopp/cryptlib.h>

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class KeyAgreement

class Cipher:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._activated_ = False
        self._encoder_ = None
        self._decoder_ = None
        self._key_agreement_ = None

        self._activated_ = DefineConstants.false
        self._encoder_ = None
        self._decoder_ = None
        self._key_agreement_ = None

    def close(self):
        if self._activated_:
            self.CleanUp()

    def CleanUp(self):
        if self._encoder_ is not None:
            self._encoder_ = None
            self._encoder_ = None
        if self._decoder_ is not None:
            self._decoder_ = None
            self._decoder_ = None
        if self._key_agreement_ is not None:
            if self._key_agreement_ is not None:
                self._key_agreement_.close()
            self._key_agreement_ = None
        self._activated_ = DefineConstants.false

    def Prepare(self, buffer, length):
        key_agreement_ is None
        key_agreement_ = DH2KeyAgreement()
        assert key_agreement_ is not None
        agreed_length = key_agreement_.Prepare(buffer, length)
        if agreed_length == 0:
            key_agreement_ = None
            key_agreement_ = None
        return size_t(agreed_length)

    def Activate(self, polarity, agreed_length, buffer, length):
        activated_ is DefineConstants.false
        assert self._key_agreement_ is not None
        if activated_ is not DefineConstants.false:
            return DefineConstants.false

        if self._key_agreement_.Agree(size_t(agreed_length), buffer, size_t(length)):
            activated_ = self._SetUp(polarity)
        if self._key_agreement_ is not None:
            self._key_agreement_.close()
        self._key_agreement_ = None
        return activated_ is not None

    def Encrypt(self, buffer, length):
        activated_ = assert()
        if activated_ is None:
            return
        self._encoder_.ProcessData(int(buffer), int(buffer), length)

    def Decrypt(self, buffer, length):
        activated_ = assert()
        if activated_ is None:
            return
        self._decoder_.ProcessData(int(buffer), int(buffer), length)

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool activated() const
    def activated(self):
        return self._activated_
    def set_activated(self, value):
        self._activated_ = value

    def IsKeyPrepared(self):
        return self._key_agreement_ is not None

    def _SetUp(self, polarity):
        assert self._key_agreement_ is not None
        shared = self._key_agreement_.shared()

        if shared.size() < 2:
            return DefineConstants.false
        hint_0 = shared.BytePtr()[math.fmod(*(shared.BytePtr()), shared.size())]
        hint_1 = shared.BytePtr()[math.fmod(*(shared.BytePtr() + 1), shared.size())]
        detail_0 = BlockCipherAlgorithm.Pick(hint_0)
        detail_1 = BlockCipherAlgorithm.Pick(hint_1)
        assert detail_0 is not None
        assert detail_1 is not None
        algorithm_0 = std::unique_ptr(detail_0)
        algorithm_1 = std::unique_ptr(detail_1)

        key_length_0 = algorithm_0.GetDefaultKeyLength()
        iv_length_0 = algorithm_0.GetBlockSize()
        if shared.size() < key_length_0 or shared.size() < iv_length_0:
            return DefineConstants.false
        key_length_1 = algorithm_1.GetDefaultKeyLength()
        iv_length_1 = algorithm_1.GetBlockSize()
        if shared.size() < key_length_1 or shared.size() < iv_length_1:
            return DefineConstants.false

        key_0 = SecByteBlock(key_length_0)
        iv_0 = SecByteBlock(iv_length_0)
        key_1 = SecByteBlock(key_length_1)
        iv_1 = SecByteBlock(iv_length_1)

        offset = size_t()

        key_0.Assign(shared, key_length_0)
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: offset = key_length_0;
        offset.copy_from(key_length_0)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no preprocessor in Python:
##if __GNUC__
        offset = min(key_length_0, shared.size() - key_length_1)
##else
        offset = min(key_length_0, shared.size() - key_length_1)
##endif
        key_1.Assign(shared.BytePtr() + offset, key_length_1)

        offset = shared.size() - iv_length_0
        iv_0.Assign(shared.BytePtr() + offset, iv_length_0)
        offset = (0 if offset < iv_length_1 else offset - iv_length_1)
        iv_1.Assign(shared.BytePtr() + offset, iv_length_1)


        if polarity:
            self._encoder_ = algorithm_1.CreateEncoder(key_1, key_1.size(), iv_1)
            self._decoder_ = algorithm_0.CreateDecoder(key_0, key_0.size(), iv_0)
        else:
            self._encoder_ = algorithm_0.CreateEncoder(key_0, key_0.size(), iv_0)
            self._decoder_ = algorithm_1.CreateDecoder(key_1, key_1.size(), iv_1)
        assert self._encoder_ is not None
        assert self._decoder_ is not None
        return ((not DefineConstants.false))




class BlockCipherAlgorithm:
    KDEFAULT = 0
    KRC6 = 1
    KMARS = 2
    KTWOFISH = 3
    KSERPENT = 4
    KCAST256 = 5
    KIDEA = 6
    K3DES = 7
    KCAMELLIA = 8
    KSEED = 9
    KRC5 = 10
    KBLOWFISH = 11
    KTEA = 12
    KSHACAL2 = 13
    KMAXALGORITHMS = 14

    def __init__(self):
        pass
    def close(self):
        pass

    @staticmethod
    def Pick(hint):
        detail = None
        selector = math.fmod(hint, KMAXALGORITHMS)

        if selector == KRC6:
            detail = BlockCipherDetail()
        elif selector == KMARS:
            detail = BlockCipherDetail()
        elif selector == KTWOFISH:
            detail = BlockCipherDetail()
        elif selector == KSERPENT:
            detail = BlockCipherDetail()
        elif selector == KCAST256:
            detail = BlockCipherDetail()
        elif selector == KIDEA:
            detail = BlockCipherDetail()
        elif selector == K3DES:
            detail = BlockCipherDetail()
        elif selector == KCAMELLIA:
            detail = BlockCipherDetail()
        elif selector == KSEED:
            detail = BlockCipherDetail()
        elif selector == KRC5:
            detail = BlockCipherDetail()
        elif selector == KBLOWFISH:
            detail = BlockCipherDetail()
        elif selector == KTEA:
            detail = BlockCipherDetail()
        elif selector == KSHACAL2:
            detail = BlockCipherDetail()
        else:
            detail = BlockCipherDetail()
        return detail

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual int GetBlockSize() const = 0;
    def GetBlockSize(self):
        pass
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual int GetDefaultKeyLength() const = 0;
    def GetDefaultKeyLength(self):
        pass
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual int GetIVLength() const = 0;
    def GetIVLength(self):
        pass

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual SymmetricCipher* CreateEncoder(const byte* key, size_t keylen, const byte* iv) const = 0;
    def CreateEncoder(self, key, keylen, iv):
        pass
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual SymmetricCipher* CreateDecoder(const byte* key, size_t keylen, const byte* iv) const = 0;
    def CreateDecoder(self, key, keylen, iv):
        pass

class BlockCipherDetail(BlockCipherAlgorithm):
    def __init__(self):
        pass
    def close(self):
        pass

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual int GetBlockSize() const
    def GetBlockSize(self):
        return T.BLOCKSIZE
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual int GetDefaultKeyLength() const
    def GetDefaultKeyLength(self):
        return T.DEFAULT_KEYLENGTH
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual int GetIVLength() const
    def GetIVLength(self):
        return T.IV_LENGTH

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual SymmetricCipher* CreateEncoder(const byte* key, size_t keylen, const byte* iv) const
    def CreateEncoder(self, key, keylen, iv):
        return typename CTR_Mode.Encryption(key, keylen, iv)
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: virtual SymmetricCipher* CreateDecoder(const byte* key, size_t keylen, const byte* iv) const
    def CreateDecoder(self, key, keylen, iv):
        return typename CTR_Mode.Decryption(key, keylen, iv)

class KeyAgreement:
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.shared_ = SecByteBlock()

    def close(self):
        pass

    def Prepare(self, buffer, length):
        pass
    def Agree(self, agreed_length, buffer, length):
        pass

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: const SecByteBlock& shared() const
    def shared(self):
        return SecByteBlock(self.shared_)


class DH2KeyAgreement(KeyAgreement):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._dh_ = DH()
        self._dh2_ = DH2()
        self._spriv_key_ = SecByteBlock()
        self._epriv_key_ = SecByteBlock()

        self._dh_ = DH()
        self._dh2_ = self._dh_

    def close(self):
        pass

    def Prepare(self, buffer, length):
        p = Integer("0xB10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C6" + "9A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C0" + "13ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD70" + "98488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0" + "A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708" + "DF1FB2BC2E4A4371")

        g = Integer("0xA4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507F" + "D6406CFF14266D31266FEA1E5C41564B777E690F5504F213" + "160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1" + "909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28A" + "D662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24" + "855E6EEB22B3B2E5")

        q = Integer("0xF518AA8781A8DF278ABA4E7D64B7CB9D49462353")

        rnd = AutoSeededRandomPool()

        self._dh_.AccessGroupParameters().Initialize(p, q, g)

        if not self._dh_.GetGroupParameters().ValidateGroup(rnd, 3):
            return 0

        p = self._dh_.GetGroupParameters().GetModulus()
        q = self._dh_.GetGroupParameters().GetSubgroupOrder()
        g = self._dh_.GetGroupParameters().GetGenerator()

        v = ModularExponentiation(g, q, p)
        if v is not Integer.One():
            return 0

        self._spriv_key_.New(self._dh2_.StaticPrivateKeyLength())
        self._epriv_key_.New(self._dh2_.EphemeralPrivateKeyLength())
        spub_key = SecByteBlock(self._dh2_.StaticPublicKeyLength())
        epub_key = SecByteBlock(self._dh2_.EphemeralPublicKeyLength())

        self._dh2_.GenerateStaticKeyPair(rnd, self._spriv_key_, spub_key)
        self._dh2_.GenerateEphemeralKeyPair(rnd, self._epriv_key_, epub_key)

        spub_key_length = spub_key.size()
        epub_key_length = epub_key.size()
        data_length = spub_key_length + epub_key_length
        if length < data_length:
            return 0
## Laniatus Games Studio Inc. | ROLE OF DEVELOPMENT SECTION: The following line has been determined to be tokenless assignment (rather than reference assignment) - this should be verified and a 'copy_from' method should be created: For this, follow the instructions from the dependencies addendum convteam@laniatusgames.com.
#ORIGINAL METINII C CODE: *length = data_length;
        length.copy_from(data_length)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: byte* buf = (byte*)buffer;
        buf = byte(int(buffer))
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memcpy(buf, spub_key.BytePtr(), spub_key_length)
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
        memcpy(buf + spub_key_length, epub_key.BytePtr(), epub_key_length)

        return self._dh2_.AgreedValueLength()

    def Agree(self, agreed_length, buffer, length):
        if agreed_length is not self._dh2_.AgreedValueLength():
            return DefineConstants.false
        spub_key_length = self._dh2_.StaticPublicKeyLength()
        epub_key_length = self._dh2_.EphemeralPublicKeyLength()
        if length is not (spub_key_length + epub_key_length):
            return DefineConstants.false
        self.shared_.New(self._dh2_.AgreedValueLength())
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: const byte* buf = (const byte*)buffer;
        buf = byte(int(buffer))
        if not self._dh2_.Agree(self.shared_, self._spriv_key_, self._epriv_key_, buf, buf + spub_key_length):
            return DefineConstants.false
        return ((not DefineConstants.false))


##endif
