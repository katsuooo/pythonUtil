# coding: shift-jis
'''
qrcode ����
'''

import qrcode, os				# ���C�u�����ǂݍ���
file_name = "qr_code.png"		#�ۑ�����QR�R�[�h�̃t�@�C����
print("QR�R�[�h�ɕϊ����������������͂��Ă�������: ", end="")
#qr_string = input()				# �L�[�{�[�h����ϊ����������������͂�����
qr_string = '���Y���V'
img = qrcode.make(qr_string)		# QR�R�[�h�摜�f�[�^����
img.save(file_name)				# �摜�t�@�C���Ƃ��ĕۑ�
current_dir = os.getcwd()			# ���݂̃f�B���N�g���ʒu���擾
print("�u{0}\\{1}�v��QR�R�[�h�摜��ۑ����܂���".format(current_dir, file_name))	# �I�����b�Z�[�W�o��
