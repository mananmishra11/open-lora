# OpenLoRa Implementation

**config.py:** Set up the configuration for LoRa.
RX_Sampl_Rate: Sampling rate for the input data
LORA_BW: Bandwidth
LORA_SF: Spreading factor
Packet_Time: Total duration of the input dataset in seconds
Packets_Num: Total number of packets in the input data (= Transmission rate of one node * Number of nodes in network * Packet_Time)
input_file: Path to the input data file
true_sym: Ground truth for the demodulated symbols transmitted by the LoRa node
true_msg: Ground truth for the decoded bits transmitted by the LoRa node

**master.py:** Call the demodulators to process input data
Std-LoRa: demod.std_lora()
CoLoRa: demod.colora()
FTrack: demod.ftrack()
NScale: demod.nscale()
CIC: demod.cic()

**demod.py:** Includes the 'main' file from each demodulator implementation to be called in the master file

**decode.py:** LoRa decoder implementation to input demodulated symbols and output decoded bits.

**metrics.py:** Takes the demodulated symbols as input and calls the decoder to find out various metrics. Prints out Symbols Error Rate (SER), Bit Error Rate (BER), Packet Detection Rate (PDR) and Throughtput (in bits/s)

## Docker Configuration:

### Running with custom dataset:
1. Clone the git repo.
2. Copy the desired data file to the folder where local git repo is cloned.
3. Change the configuration in *config.py*, setting up parameters for the desired dataset.
4. Run the following docker command:
> docker build --tag open-lora
5. Finally, use the following commannd to run the framework with the new dataset.
> docker run open-lora

### Running with included dataset:
The included data file *sf8_125_1pps.data* can also be used to run the framework as is.
The docker image can be found [here](https://hub.docker.com/r/mananmishra11/open-lora).
Run the following commands ro run the docker image:
> docker pull mananmishra11/open-lora

> docker run mananmishra11/open-lora


