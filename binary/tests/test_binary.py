from binary import Binary
import pytest

def test_binary_init_int():
	binary = Binary(6)
	assert int(binary) == 6

def test_binary_init_binstr():
    binary = Binary('0b110')
    assert int(binary) == 6

def test_binary_init_bitstr():
    binary = Binary('110')
    assert int(binary) == 6

def test_binary_init_hexstr():
    binary = Binary('0x6')
    assert int(binary) == 6

def test_binary_init_hex():
    binary = Binary(0x6)
    assert int(binary) == 6

def test_binry_init_intseq():
    binary = Binary([1,1,0])
    assert int(binary) == 6

def test_binary_init_strseq():
    binary = Binary(['1', '1', '0'])
    assert int(binary) == 6

def test_binary_init_negative():
    with pytest.raises(ValueError):
        binary = Binary(-4)


## Conversions

def test_binary_eq():
    assert Binary(4) == Binary(4)

def test_binary_int():
    binary = Binary(6)
    assert int(binary) == 6

def test_binary_str():
    binary = Binary(6)
    assert str(binary) == '110'

def test_binary_hex():
    binary = Binary(6)
    assert hex(binary) == '0x6'

def test_binary_bin():
    binary = Binary(6)
    assert bin(binary) == '0b110'

## Basic Operations

def test_binary_addition_int():
    assert Binary(4) + 1 == Binary(5)

def test_binary_addition_binary():
    assert Binary(4) + Binary(5) == Binary(9)

def test_binary_division_int():
    assert Binary(20) / 4 == Binary(5)

def test_bianry_division_rem_int():
    assert Binary(21) / 4 == Binary(5)

def test_binary_get_bit():
    binary = Binary('0101110001')
    assert binary[0] == '1'
    assert binary[5] == '1'
    assert binary[7] == '0'

def test_binary_not():
    assert ~Binary('1101') == Binary('10')

def test_binary_and():
    assert Binary('1101') & Binary('1') == Binary('1')

def test_binary_sh1_pos():
    assert Binary('1101') << 5 == Binary('110100000')

def test_binary_slice():
    assert Binary('01101010')[0:3] == Binary('10')
    assert Binary('01101010')[1:4] == Binary('101')
    assert Binary('01101010')[4:] == Binary('110')

def test_binary_illegal_index():
    with pytest.raises(IndexError):
        Binary('01101010')[7]

def test_binary_negative_index():
    assert Binary('0101110001')[-1] == '1'
    assert Binary('0101110001')[-2] == '0'

def test_binary_inappropriate_type_index():
    with pytest.raises(TypeError):
        Binary('01101010')['key']

def test_binary_for_loop():
    assert [int(i) for i in Binary('01101010')] == [0, 1, 0, 1, 0, 1, 1]

def test_binary_not():
    assert ~Binary('1101') == Binary('10')

def test_binary_and():
    assert Binary('1101') & Binary('1') == Binary('1')
