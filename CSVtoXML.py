import fire
import os
import csv
from PIL import Image
from pascal_voc_writer import Writer

class XMLConverter(object):

	def help(self):
		print('Below command is available: \n    python ./CSVtoXML/CSVtoXML.py convert CSVFILEPATH PICFOLDERPATH XMLFOLDERPATH\n')
		print('example: \n\tpython ./Python_Other/CSVtoXML/CSVtoXML.py convert ./Python_Other/sample.csv ./Python_Other/jpg/ ./Python_Other/xml/')


	def convert(self, file_path, picpath = './', xmlpath = './'):
		if not os.path.isfile(file_path):
			return 'File does not exist.'
		with open(file_path) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				if row['region_count'] =='1':
					self.parsing(row, picpath, xmlpath)
	
	def parsing(self, item, picpath, xmlpath):
		parstr = item['region_shape_attributes']
		x= parstr[:-1].split(',')
		nums = []
		for k in x[1:]:
			temp = int(k.split(':')[-1])
			nums.append(temp)
		fname = item['#filename']
		name = fname.split('-')[0]
		savefile = xmlpath+fname.split('.')[0]+'.xml'
		fpath = picpath+fname
		if not os.path.isfile(fpath):
			print('pic not found: '+fpath)
			return('Jump out')
		else:
			im=Image.open(fpath)
			width, height = im.size
			abspath  =os.path.abspath(fpath)
			writer = Writer(abspath, width, height)
			writer.addObject(name, nums[0], nums[1], nums[0]+nums[2], nums[1]+nums[3])
			writer.save(savefile)
			print('File '+ fname +'.xml created')


if __name__ == '__main__':
    fire.Fire(XMLConverter)
