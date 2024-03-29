import numpy as np

RX_Sampl_Rate = int(500e3)
LORA_BW = int(125e3)
LORA_SF = int(8)
Packet_Time = 30 #in seconds
Packets_Num = 1 * 20 * 30 # Packets/sec * Number of transmitters * Duration of transmission in sec
input_file = './sf8_125_1pps.data'
output_file = 'output.xlsx'

true_msg = np.array([255, 255, 0, 0, 72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 0, 152, 72]) # 'Hello World'

# CIC 'LoraPkt'
#true_sym = np.array([28,48,252,112,56,60,12,48,99,48,36,21,60,225,190,239,172,84,150,27,169,121,131,205,82,213,78,244])
#true_msg = np.array([255, 255,   0,   0,  76, 111,  82,  97,  80, 107, 116,   0,  41,  23, 156,   4,   1])

# SF8 'Hello World'
# CR 4/5
#true_sym = np.array([89, 13, 29, 13, 225, 61, 57, 209, 100, 49, 28, 22, 52, 63, 201, 221, 203, 169, 92, 179, 185, 31, 206, 41, 96, 164, 45, 73, 206, 81, 171, 242, 245])
# CR 4/6
#true_sym = np.array([ 89,   1,   5,  13, 229, 193,  37, 225, 100,  49,  28,  22, 199, 251,  63, 201, 221, 203,  51,  91,  92, 179, 185,  31,  62,  69, 41,  96, 164,  45,  95, 155, 206,  81, 171, 242, 116,  20])
# CR 4/7
#true_sym = np.array([ 37,  49,  25,  13, 157, 253,  57, 225, 100,  49,  28,  22, 199, 251, 179,  63, 201, 221, 203,  51,  91,  25,  92, 179, 185,  31, 62,  69, 200,  41,  96, 164,  45,  95, 155,  40, 206,  81, 171,242, 116,  20, 105])
# CR 4/8
true_sym = np.array([ 89,  61,  29, 241, 153, 193,  69, 221, 100,  49,  28,  22, 199, 251, 179, 186,  63, 201, 221, 203,  51,  91,  25,  55,  92, 179,
       185,  31,  62,  69, 200, 148,  41,  96, 164,  45,  95, 155,  40, 120, 206,  81, 171, 242, 116,  20, 105,  33])


# SF10 'Hello World'
#true_sym = np.array([933, 13, 29, 13, 957, 253, 237, 181, 104, 461, 826, 587, 981, 580, 813, 118, 737, 557, 162, 642, 883, 592, 802, 787, 73, 766, 948, 991])
#true_msg = [16, 49, 208, 255, 255, 0, 0, 72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 0, 152, 72, 173, 148, 235, 13]

# SF12 'Hello World'
#true_sym = np.array([933, 13, 993, 497, 3777, 1021, 945, 709, 999, 3213, 1487, 2899, 3211, 2140, 4019, 2888, 34, 3150, 3294, 1286, 683, 3311, 2225])
#true_msg = [16, 49, 208, 255, 255, 0, 0, 72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 0, 152, 72, 119, 211, 15]

Max_Payload_Num = len(true_sym)
