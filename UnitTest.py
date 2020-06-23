import unittest

#测试函数
from Function import GetFormattedName

class Test_UnitTest(unittest.TestCase):
    def test_GetFormattedName(self):
        formattedName = GetFormattedName('janis', 'joplin')
        self.assertEqual(formattedName, 'Janis Joplin')
    
    def test_GetFormattedFirstName(self):
        firstName = GetFormattedName('supent')
        self.assertEqual(firstName.rstrip(), 'Supent')


#测试类
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses=[]

    def ShowQuestion(self):
        print(question)

    def StoreResponse(self, newResponse):
        self.responses.append(newResponse)

    def ShowResults(self):
        print("Survey results:")
        for response in responses:
            print('-' + response)

class TestAnonmyousSurvey(unittest.TestCase):
    
    def test_StoreSingleResponse(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        mySurvey = AnonymousSurvey(question)
        mySurvey.StoreResponse('English')

        self.assertIn('English', mySurvey.responses)

    def test_StoreThreeResponse(self):
        question = "What language did you first learn to speak?"
        mySurvey = AnonymousSurvey(question)
        responses = ['English', 'Chinese', 'American']
        for response in responses:
            mySurvey.StoreResponse(response)

        for response in responses:
            self.assertIn(response, mySurvey.responses)


#优化测试类，只创建一个类对象
class TestAnonmyousSurveyBetter(unittest.TestCase):
    
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.mySurvey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'American']

    def test_StoreSingleResponse(self):
        self.mySurvey.StoreResponse(self.responses[0])
        self.assertIn(self.responses[0], self.mySurvey.responses)

    def test_StoreThreeResponse(self):
        for response in self.responses:
            self.mySurvey.StoreResponse(response)
        for response in self.responses:
            self.assertIn(response, self.mySurvey.responses)

if __name__ == '__main__':
    unittest.main()