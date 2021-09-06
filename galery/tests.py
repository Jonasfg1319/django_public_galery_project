from django.test import TestCase
from .models import Images
# Create your tests here.

class UploadTest(TestCase):
  
  def test_upload_field_no_string(self):
  	images = Images()
  	word, word2 = "bily", "    "
  	response = images.verify_field(word, word2)
  	self.assertEqual(response, "empty")

  def test_verify_format_jpeg(self):
  	images = Images()
  	response = images.verify_format("image/jpeg")
  	self.assertEqual(response, True)


  def test_verify_format_png(self):
  	images = Images()
  	response = images.verify_format("image/png")
  	self.assertEqual(response, True)

  def test_verify_format_gif(self):
  	images = Images()
  	response = images.verify_format("image/gif")
  	self.assertEqual(response, True)


  def test_verify_format_other(self):
  	images = Images()
  	response = images.verify_format("aplication/pdf")
  	self.assertEqual(response, False)