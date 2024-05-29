class Frase:

  def __init__(self, f: str):
    self.__frase = f;

  @property
  def frase(self) -> str:
    return self.__frase
  
  @frase.setter
  def frase(self, f:str) -> None:
    self.__frase = f

  def mayuscula(self) -> str:
    return self.__frase.upper()
  
  def minuscula(self) -> str:
    return self.__frase.lower()