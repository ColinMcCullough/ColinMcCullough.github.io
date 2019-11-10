from ch_two_exercises import *
import unittest
class TestStringMethods(unittest.TestCase): 
    """Unit tests for Fractions Class
    Arguments:
        unittest {unittest}
    """
    def test_list_index_time(self):
        self.assertIsInstance(list_index_time(10000,100001,10000), dict) 
        self.assertEqual(len(list_index_time(10000,100001,10000)),10)

    def test_get_indx_time(self):
        lst = [1,2,3,4,5,6,7,8,9,10]
        indx = 2
        self.assertIsInstance(get_indx_time(lst,indx), float)
        with self.assertRaises(IndexError):
            get_indx_time(lst,100)

    def test_dictionary_get_time(self):
        self.assertIsInstance(dictionary_get_time(10000,100001,10000), dict)
        self.assertEqual(len(dictionary_get_time(10000,100001,10000)),10)
        self.assertEqual(len(dictionary_get_time(1000,100001,1000)),100)  

    def test_dictionary_set_time(self):
        self.assertIsInstance(dictionary_set_time(10000,100001,10000), dict)
        self.assertEqual(len(dictionary_set_time(10000,100001,10000)),10)
        self.assertEqual(len(dictionary_set_time(1000,100001,1000)),100)

    def test_get_set_dict_time(self):
        self.assertIsInstance(get_set_dict_time({"1": None,"2":None,"3":None},2), float)
        self.assertIsInstance(get_set_dict_time({"1": None,"2":None,"3":None},100), float)
    
    def test_dictionary_get_time(self):
        x,y = lst_vs_dictionary_del_time(10000,100001,10000)
        self.assertIsInstance(x, list)
        self.assertIsInstance(y, dict)
        self.assertEqual(len(x),10)
        self.assertEqual(len(y),10)

    def test_del_lst_time(self): 
        lst = [x for x in range(1000)]
        lst2 = [x for x in range(10)]
        self.assertIsInstance(del_lst_time(lst), float)
        self.assertIsInstance(del_lst_time(lst2), float)

    def test_del_dict_time(self): 
        dct = {x:'test' for x in range(1000)}
        dct2 = {x:'test' for x in range(10)}
        self.assertIsInstance(del_dict_time(dct), float)
        self.assertIsInstance(del_dict_time(dct2), float)

    def test_find_k_smallest_n_log_n(self):
        k = 2
        k2 = 3
        lst = [0,20,8,15]
        self.assertEqual(find_k_smallest_n_log_n(k,lst),8)
        self.assertEqual(find_k_smallest_n_log_n(k2,lst),15)
        with self.assertRaises(TypeError):
            find_k_smallest_n_log_n(True,100)
        with self.assertRaises(Exception):
            find_k_smallest_n_log_n(2,[])
        with self.assertRaises(Exception):
            find_k_smallest_n_log_n(5,[0,20,10,3])

    
    def test_gen_rndm_num_arr(self):
        self.assertEqual(len(gen_rndm_num_arr(10)),10)
        self.assertEqual(len(gen_rndm_num_arr(100)),100)



if __name__ == '__main__':
    unittest.main()