from django.db import models
import hashlib

'''
    进行密码加密
'''


def hash_password(password):
    # isinstance(password, str)  把password转换为字符串
    if isinstance(password, str):
        # encode() 方法以 encoding 指定的编码格式编码字符串
        password = password.encode('utf-8')

    # 将明文密码通过md5进行加密,返回一个加密后的md5的值
    password_hash = hashlib.md5(password).hexdigest().upper()
    return password_hash


'''
    创建客户端用户表
'''


class ClientUser(models.Model):
    # 用户名
    username = models.CharField(max_length=50, null=False, unique=True)
    # 密码
    password = models.CharField(max_length=255, null=False)
    # 头像
    avatar = models.CharField(max_length=500, default='')
    # 性别
    sex = models.CharField(max_length=10, default='')
    # 出生年月
    birthday = models.DateTimeField(null=True, blank=True, default=None)
    # 状态
    status = models.BooleanField(default=True, db_index=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'username:{}'.format(self.username)

    # 创建
    @classmethod
    def add(cls, username, password, avatar='', sex='', birthday=None):
        return cls.objects.create(
            username=username,
            password=hash_password(password),
            avatar=avatar,
            sex=sex,
            status=True
        )

    # 获取
    @classmethod
    def get_user(cls, username, password):
        try:
            user = cls.objects.get(
                username=username,
                password=hash_password(password),
            )
        except:
            return None

    # 修改密码
    def update_password(self, old_password, new_password):
        hash_old_password = hash_password(old_password)
        if hash_old_password != self.password:
            return False
        hash_new_password = hash_password(new_password)
        self.password = hash_new_password
        self.save()
        return True

    # 修改用户状态
    def update_status(self):
        self.status = not self.status
        self.save()
        return True


'''
    视频类型表
'''


class VideoType(models.Model):
    type_name = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return 'type_name:'.format(self.type_name)


'''
    视频来源表
'''


class FromTo(models.Model):
    from_to = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return 'from_to:'.format(self.from_to)


class Nationality(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return 'name:{}'.format(self.name)


'''
    创建视频表
'''


class Video(models.Model):
    # 名字
    name = models.CharField(max_length=100, null=False)
    # 视频海报
    image = models.CharField(max_length=500, default='')
    # 视频类型
    video_type = models.ForeignKey(
        VideoType, related_name='video_type', on_delete=models.CASCADE, null=False)
    # 视频来源
    from_to = models.ForeignKey(
        FromTo, related_name='video_from', on_delete=models.CASCADE, null=False)
    # 国籍
    nationality = models.ForeignKey(
        Nationality, related_name='video_nationality', on_delete=models.CASCADE, null=False)
    # 简介
    info = models.TextField()
    # 视频状态
    status = models.BooleanField(default=True, db_index=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 最后一次修改时间
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'video_type', 'from_to', 'nationality')

    def __str__(self):
        return self.name


'''
    演员表
'''


class VideoStar(models.Model):
    # 视频
    video = models.ForeignKey(
        Video,
        related_name='video_star',
        on_delete=models.CASCADE,
        blank=True, null=False
    )
    # 演员姓名
    name = models.CharField(max_length=100, null=False)
    # 身份
    identity = models.CharField(max_length=50, default='')

    class Meta:
        unique_together = ('video', 'name', 'identity')


class VideoSub(models.Model):
    # 视频
    video = models.ForeignKey(
        Video,
        related_name='video_sub',
        on_delete=models.CASCADE,
        blank=True, null=False
    )
    url = models.CharField(max_length=500, null=False)
    number = models.IntegerField(default=1)

    def __str__(self):
        return 'video:{},number:{}'.format(self.video.name, self.number)
