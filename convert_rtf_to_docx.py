import os.path
import win32com.client

baseDir = r'C:\Users\Катя\Desktop\рпд'

word = win32com.client.Dispatch("Word.application")

for dir_path, dirs, files in os.walk(baseDir):
	for file_name in files:
		file_path = os.path.join(dir_path, file_name)
		file_name, file_extension = os.path.splitext(file_path)
		if file_extension.lower() == '.rtf':
			docx_file = '{0}{1}'.format(file_name, '.docx')
			if not os.path.isfile(docx_file):
				print('Converting: {0}'.format(file_path))
				try:
					wordDoc = word.Documents.Open(file_path, False, False, False)
					wordDoc.SaveAs2(docx_file, FileFormat = 16)
					wordDoc.Close()
				except Exception:
					print('Failed to Convert: {0}'.format(file_path))

word.Quit()