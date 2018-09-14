import unittest

class TestStringMethods(unittest.TestCase):

    def test_merge(self):
        self.assertEqual(merge_str("javascript", "javpt", "ascri"), 1)
        self.assertEqual(merge_str("javascript", "jasrit", "vacp"), 1)
        self.assertEqual(merge_str("javascript", "java", "scripts"), 0)
        self.assertEqual(merge_str("javascript", "jav", "script"), 0)
        self.assertEqual(merge_str("java not script", "java ", "not script"),1)
        self.assertEqual(merge_str("javascript", "java", "scriptp"), 0)
        self.assertEqual(merge_str("Java1Java3Java1Java3", "Java1Java3", "Java1Java3"), 1)
        self.assertEqual(merge_str('Bananas from Bahamas', 'Bahas', 'Bananas from am'), 1)
        self.assertEqual(merge_str('codewars','cwdr','oeas'), 0)
        self.assertEqual(merge_str("?#'G[tUqc%qeyS4lx4fJWc^&6","?#[%ey4xJ^&6","'GtUqcqSl4fWc"),1)
        self.assertEqual(merge_str("ca","c","ab"),0)
        self.assertEqual(merge_str("cc","c","c"),1)
        self.assertEqual(merge_str("Java1Java1", "Java1", "ava1"), 0)



def merge_str(merge, str1, str2):
    if len(merge) != (len(str1) + len(str2)):
        return 0
    i = k = l = m = 0
    while i != len(merge):
        if k!=len(str1) and l!=len(str2):
            if merge[i] != str1[k] and merge[i] != str2[l]:
                return 0
            else:
                if merge[i] == str1[k] and merge[i] == str2[l]:
                    i += 1
                    k += 1
                    l += 1
                    m += 1
                    if l == len(str2):
                        l -= m
                        m = 0
                    if k == len(str1):
                        k -= m
                        m = 0
                else:
                    if merge[i] == str1[k]:
                        i += 1
                        k += 1
                        l -= m
                        m = 0
                    else:
                        k -= m
                        m = 0
                        if merge[i] == str2[l]:
                            i += 1
                            l += 1
                            k -= m
                            m = 0
                        else:
                            l -= m
                            m = 0
        elif k == len(str1):
            if merge[i] == str2[l]:
                i += 1
                l += 1
            else:
                return 0
        elif l == len(str2):
            if merge[i] == str1[k]:
                i += 1
                k += 1
            else:
                return 0

    if k!= len(str1) or l!= len(str2):
        return 0
    else:
        return 1


unittest.main()
