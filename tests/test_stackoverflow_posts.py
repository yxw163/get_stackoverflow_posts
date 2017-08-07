# -*- coding: utf-8 -*-

import unittest, json
from stackoverflow_posts import app

class StackoverflowTestCase(unittest.TestCase):
	def setUp(self):
		app.testing = True
		self.app = app.test_client()

	def tearDown(self):
		pass


	def test_get_posts(self):
		rv = self.app.post('/userposts', 
							data=json.dumps({'userId': '1'}), 
							content_type='application/json')
		self.assertEqual(rv.status_code, 200)
		self.assertIn(b'14', rv.data)
	
	def test_post_with_wrong_userid(self):
		rv = self.app.post('/userposts', 
							data=json.dumps({'userId': '1a'}), 
							content_type='application/json')

		self.assertEqual(rv.status_code, 200)
		self.assertIn(b'no method found with this name', rv.data)

	def test_post_with_unexist_userid(self):
		rv = self.app.post('/userposts', 
							data=json.dumps({'userId': '12'}), 
							content_type='application/json')
		self.assertEqual(rv.status_code, 200)
		self.assertListEqual(json.loads(rv.data.decode('utf-8'))['items'], [])


if __name__ == '__main__':
	unittest.main()