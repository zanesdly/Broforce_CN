import struct;
import string;
import csv;

INT_LEN = 4;
UINT_LEN = 4;
LONG_LEN = 8;

def get_file_size(f):
	pos = f.tell();
	f.seek(0, 2);
	size = f.tell();
	f.seek(pos, 0);
	return size;

def aligned_stream(f, alignment):
	pos = f.tell();
	mod = pos % alignment;
	if (mod != 0):
		f.write('\x00' * (alignment - mod));

def write_aligned_str(f, str):
	str_len = len(bytes(str));
	f.write(struct.pack("<i", str_len));
	f.write(str);
	aligned_stream(f, 4);

def serialize_stringbank(file_name):
	gameobj_fielID = 0;
	gameobj_pathID = 0;
	gameobj_enabled = 0;
	script_fielID = 0;
	script_pathID = 0;
	script_name = 0;
	pair_len = 0;
	key_arr = [];
	value_arr = [];

	f = open(file_name + '.csv', 'r');
	csv_reader = csv.reader(f);
	
	gameobj_fielID = string.atoi(csv_reader.next()[2]);
	gameobj_pathID = string.atof(csv_reader.next()[2]);
	gameobj_enabled = string.atoi(csv_reader.next()[2]);
	script_fielID = string.atoi(csv_reader.next()[2]);
	script_pathID = string.atof(csv_reader.next()[2]);
	script_name = csv_reader.next()[2]
	
	for row in csv_reader:
		pair_len += 1;
		key_arr.append(row[0]);
		value_arr.append(row[2]);
	
	f.close();
	
	f = open(file_name + '.se.dat', 'wb');
	
	f.write(struct.pack("<i", gameobj_fielID));
	f.write(struct.pack("<q", gameobj_pathID));
	f.write(struct.pack("<I", gameobj_enabled));
	f.write(struct.pack("<i", script_fielID));
	f.write(struct.pack("<q", script_pathID));
	write_aligned_str(f, script_name);
	f.write(struct.pack("<I", pair_len));

	for i in range(pair_len):
		write_aligned_str(f, key_arr[i]);
		write_aligned_str(f, value_arr[i]);
	
	f.close();
	return;

serialize_stringbank('266');