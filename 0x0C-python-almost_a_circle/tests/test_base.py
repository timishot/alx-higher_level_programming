
                                    import unittest

                                    from models.base import Base

                                    from models.rectangle import Rectangle

                                    from models.square import Square





                                    class TestBase_instantiation(unittest.TestCase):

                                            """Unittests for testing instantiation of the Base class."""



                                                def test_no_arg(self):

                                                            b1 = Base()

                                                                    b2 = Base()

                                                                            self.assertEqual(b1.id, b2.id - 1)



                                                                                def test_three_bases(self):

                                                                                            b1 = Base()

                                                                                                    b2 = Base()

                                                                                                            b3 = Base()

                                                                                                                    self.assertEqual(b1.id, b3.id - 2)



                                                                                                                        def test_None_id(self):

                                                                                                                                    b1 = Base(None)

                                                                                                                                            b2 = Base(None)

                                                                                                                                                    self.assertEqual(b1.id, b2.id - 1)



                                                                                                                                                        def test_unique_id(self):

                                                                                                                                                                    self.assertEqual(12, Base(12).id)



                                                                                                                                                                        def test_nb_instances_after_unique_id(self):

                                                                                                                                                                                    b1 = Base()

                                                                                                                                                                                            b2 = Base(12)

                                                                                                                                                                                                    b3 = Base()

                                                                                                                                                                                                            self.assertEqual(b1.id, b3.id - 1)



                                                                                                                                                                                                                def test_id_public(self):

                                                                                                                                                                                                                            b = Base(12)

                                                                                                                                                                                                                                    b.id = 15

                                                                                                                                                                                                                                            self.assertEqual(15, b.id)



                                                                                                                                                                                                                                                def test_nb_instances_private(self):

                                                                                                                                                                                                                                                            with self.assertRaises(AttributeError):

                                                                                                                                                                                                                                                                            print(Base(12).__nb_instances)



                                                                                                                                                                                                                                                                                def test_str_id(self):

                                                                                                                                                                                                                                                                                            self.assertEqual("hello", Base("hello").id)



                                                                                                                                                                                                                                                                                                def test_float_id(self):

                                                                                                                                                                                                                                                                                                            self.assertEqual(5.5, Base(5.5).id)



                                                                                                                                                                                                                                                                                                                def test_complex_id(self):

                                                                                                                                                                                                                                                                                                                            self.assertEqual(complex(5), Base(complex(5)).id)



                                                                                                                                                                                                                                                                                                                                def test_dict_id(self):

                                                                                                                                                                                                                                                                                                                                            self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)



                                                                                                                                                                                                                                                                                                                                                def test_bool_id(self):

                                                                                                                                                                                                                                                                                                                                                            self.assertEqual(True, Base(True).id)



                                                                                                                                                                                                                                                                                                                                                                def test_list_id(self):

                                                                                                                                                                                                                                                                                                                                                                            self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)



                                                                                                                                                                                                                                                                                                                                                                                def test_tuple_id(self):

                                                                                                                                                                                                                                                                                                                                                                                            self.assertEqual((1, 2), Base((1, 2)).id)



                                                                                                                                                                                                                                                                                                                                                                                                def test_set_id(self):

                                                                                                                                                                                                                                                                                                                                                                                                            self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)



                                                                                                                                                                                                                                                                                                                                                                                                                def test_frozenset_id(self):

                                                                                                                                                                                                                                                                                                                                                                                                                            self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)



                                                                                                                                                                                                                                                                                                                                                                                                                                def test_range_id(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                            self.assertEqual(range(5), Base(range(5)).id)



                                                                                                                                                                                                                                                                                                                                                                                                                                                def test_bytes_id(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.assertEqual(b'Python', Base(b'Python').id)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                def test_bytearray_id(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def test_memoryview_id(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def test_inf_id(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.assertEqual(float('inf'), Base(float('inf')).id)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def test_NaN_id(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.assertNotEqual(float('nan'), Base(float('nan')).id)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def test_two_args(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            with self.assertRaises(TypeError):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Base(1, 2)





                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            class TestBase_to_json_string(unittest.TestCase):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    """Unittests for testing to_json_string method of Base class."""



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        def test_to_json_string_rectangle_type(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    r = Rectangle(10, 7, 2, 8, 6)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def test_to_json_string_rectangle_one_dict(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            r = Rectangle(10, 7, 2, 8, 6)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        def test_to_json_string_rectangle_two_dicts(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    r1 = Rectangle(2, 3, 5, 19, 2)

??? from here until ???END lines may have been inserted/deleted
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            r2 = Rectangle(4, 2, 4, 1, 12)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    list_dicts = [r1.to_dictionary(), r2.to_dictionary()]

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def test_to_json_string_square_type(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            s = Square(10, 2, 3, 4)
???END
