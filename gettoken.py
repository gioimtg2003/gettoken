o
    e�a  �                	   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ dZdZdZ	dZ
dZdZd	Zd
Ze�d� dd� Zd�g d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d�e� �d��Zee� e�d� 	 eee� de� de� ���Zeee� de� de� de� ���Zeee�Zedkr�eed � e�d!� need"� eee� dS q�)#�    N)�datetimez[1;37mz[1;91mz[95mz[1;94mz[92mz[93mz[1;95mz[1;96m�clearc                 C   s�   ddddddddd	d
dd| d�}|dkrt jd|d�j}n|dkr+t jd| |d�j}|�d�dkr@||�d�d � �d�d S |�d�dkrPt|�d�� dS d S )Nzbusiness.facebook.comz	max-age=0z?0z	"Windows"�1zrMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zsame-originZnavigatez?1Zdocumentz#vi,vi-VN;q=0.9,en-US;q=0.8,en;q=0.7)Z	authorityzcache-controlzsec-ch-ua-mobilezsec-ch-ua-platformzupgrade-insecure-requestsz
user-agentZacceptzsec-fetch-sitezsec-fetch-modezsec-fetch-userzsec-fetch-destzaccept-language�cookie� z0https://business.facebook.com/business_locations)�headersz:https://business.facebook.com/business_locations/?page_id=ZEAAGr   �"�����F)�requests�get�text�find�split�print)r   �idpager   Zresponse� r   �gettoken.py�gettoken   s0   ��r   r   �
�[u   ●z] z	Tool By: u   [1;96mNguyễn Công Giới
zZalo: z[1;96m0367093723
zTool Get Token Free
u#   Vui lòng làm theo hướng dẫn
�   Tu   ➽ u   Nhập cookie facebook: u   Nhập id page Fbu#   (Nếu có tài khoản business): Fz
Sai cookie�   u   Thành công)r
   �os�time�sysZrandomZjsonr   ZwhiteZredZmautimZblueZgreenZvangZpinkZxanhnhat�systemr   �joinZintror   �sleep�str�inputr   r   �zr   r   r   r   �<module>   sp   0 

���������������
"



�