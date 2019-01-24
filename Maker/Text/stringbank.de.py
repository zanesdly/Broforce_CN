import struct;
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
		f.seek(alignment - mod, 1);
	
def read_aligned_str(f, len = None):
	if len is None:
		len = struct.unpack("<i", f.read(INT_LEN))[0];

	if(len > 0 and len <= (get_file_size(f) - f.tell())):
		str = f.read(len);
		aligned_stream(f, 4);
		return str;
	return "";

def deserialize_stringbank(file_name):
	gameobj_fielID = 0;
	gameobj_pathID = 0;
	gameobj_enabled = 0;
	script_fielID = 0;
	script_pathID = 0;
	script_name = 0;
	pair_len = 0;
	key_arr = [];
	value_arr = [];

	f = open(file_name + '.dat', 'rb');

	gameobj_fielID = struct.unpack("<i", f.read(INT_LEN))[0];
	gameobj_pathID = struct.unpack("<q", f.read(LONG_LEN))[0];
	gameobj_enabled = struct.unpack("<I", f.read(UINT_LEN))[0];
	script_fielID = struct.unpack("<i", f.read(INT_LEN))[0];
	script_pathID = struct.unpack("<q", f.read(LONG_LEN))[0]
	script_name = read_aligned_str(f);
	pair_len = struct.unpack("<I", f.read(UINT_LEN))[0];

	for i in range(pair_len):
		key_arr.append(read_aligned_str(f));
		value_arr.append(read_aligned_str(f));

	f.close();

	f = open(file_name + '.de.csv', 'wb');
	csv_writer = csv.writer(f);
	
	csv_writer.writerow(["gameobj_fielID", gameobj_fielID]);
	csv_writer.writerow(["gameobj_pathID", gameobj_pathID]);
	csv_writer.writerow(["gameobj_enabled", gameobj_enabled]);
	csv_writer.writerow(["script_fielID", script_fielID]);
	csv_writer.writerow(["script_pathID", script_pathID]);
	csv_writer.writerow(["script_name", script_name]);
	
	for i in range(pair_len):
		csv_writer.writerow([key_arr[i], value_arr[i]]);

	f.close();

deserialize_stringbank('261');