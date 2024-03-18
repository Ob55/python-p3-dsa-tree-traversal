from tree import Tree

class TestTree:
    '''Class for testing Tree methods'''

    def test_get_element_by_id(self):
        '''Test get_element_by_id method'''
      
        tree = Tree({
            'tag_name': 'body',
            'id': None,
            'children': [
                {
                    'tag_name': 'div',
                    'id': 'main',
                    'children': [
                        {
                            'tag_name': 'h1',
                            'id': 'heading',
                            'text_content': 'Title',
                            'children': []
                        },
                        {
                            'tag_name': 'h2',
                            'id': None,
                            'text_content': 'Subtitle',
                            'children': []
                        }
                    ]
                }
            ]
        })

        # Test cases
        assert tree.get_element_by_id('heading') == {
            'tag_name': 'h1',
            'id': 'heading',
            'text_content': 'Title',
            'children': []
        }

        assert tree.get_element_by_id('nope') is None

if __name__ == '__main__':
  
    tester = TestTree()
    tester.test_get_element_by_id()
