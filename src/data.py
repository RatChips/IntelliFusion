# data.py | IntelliFusion Version 0.1.7(202307292000) Developer Alpha
from pathlib import Path
from loguru import logger
from sqlalchemy import Column, Index, Integer, String, UniqueConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 基础类
APP_DIR = Path(__file__).parent
DATA_DIR = APP_DIR / "data"
DATABASE_FILE = DATA_DIR / "models.sqlite"

Base = declarative_base()
engine = create_engine(f"sqlite:///{DATABASE_FILE}", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class userInfo(Base):
    # 数据库中存储的表名
    __tablename__ = "userInfo"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    account = Column(String(32), index=True, nullable=False, comment="姓名")
    password = Column(String(32), nullable=False, comment="密码")
    mail = Column(String(32), index=True, nullable=True, comment="邮箱")
    __table__args__ = (
        UniqueConstraint("id", "name"),  # 联合唯一约束
        Index("name", unique=True),       # 联合唯一索引
    )



    def __str__(self):
        return f"object : <id:{self.id} name:{self.name} key:{self.key}>"


class models(Base):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    order = Column(Integer, nullable=False, comment="排序")
    type = Column(String(32), nullable=False, comment="类型")
    name = Column(String(32), nullable=False, comment="模型")
    url = Column(String(32), nullable=False, comment="地址")
    APIkey = Column(Integer, nullable=False, comment="密钥")
    LaunchCompiler = Column(String(32), nullable=True, comment="启动编译器")
    LaunchUrl = Column(String(32), nullable=True, comment="启动地址")
    Display = Column(String(32), nullable=True, comment="显示")
    __table__args__ = (
        UniqueConstraint("id", "url"),  # 联合唯一约束
        Index("url", unique=True),       # 联合唯一索引
    )

    def __str__(self):
        return f"object : <id:{self.id} url:{self.url}>"


def SetupDatabase():
    Base.metadata.create_all(engine)
    user_instance = userInfo(
        account="admin",
        password="admin1234",
    )
    session.add(user_instance)
    BasisModel = models(
        order=1,
        type="OpenAI",
        name="text-davinci-003",
        url="https:\\\\ai.fakeopen.com\\v1",
        APIkey="None",
        LaunchCompiler="NONE",
        LaunchUrl="NONE",
    )
    session.add(BasisModel)
    session.commit()

