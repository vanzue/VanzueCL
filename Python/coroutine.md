## Async IO 		<a href="https://lotabout.me/2017/understand-python-asyncio/"><font size=4 color = "gray">Check Original  Blog</font></a>

### Event Loop

<HR size=3>

* 协程是一种可以暂停的函数。
  * 等待连接建立
  * 等待socket接收消息s
  * 等待计时器归零
  * 等等
  
* 操作系统支持基于中断的方式通知应用程序      <small>(select,epoll,kqueue)</small>
  ```python
    while True:
      happened=poll_events(events_to_listen, timeout)
      process_events(happened)
  ```
* 那么对于一个Eventloop来说，需要支持三种操作：
  * Register event
  * Unregister event
  * Process event<br>
  
  ```python
  class Eventloop:
    def __init__(self):
      self.events_to_listen=[]
      self.timeout=None
      self.callback={}
    def register_event(self,event,callback):
      self.events_to_listen.append(event)
      self.callbacks[event]=callback
    def unregister_event(self,event):
      self.events_to_listen.remove(event)
      del self.callbacks[event]
    def _process_events(self,events):
      for event in events:
        self._process_events(event)
    def start_loop(self):
      while True:
        events_happened = poll_events(self.events_to_listen,self.timeout)
        self._process_events(events_happened)
  ```
 * Add time out events to event loop
   * 注册定时时间事件
   * 注册delay事件
  ```python
    def register_timeout_event(triggertime, callback):
      self._timeout_events[triggertime]=callback
    def register_delay_event(delay,callback):
      trigger_time=now().add(delay)
      self._timeout_events[]
    def start_loop(self):
      while True:
        timeout=min(self._timeout_events.keys()-now())
        events_happen=poll_events(self.events_to_listen,timeout)
        if events_happen:
          self._process_events(events_happen)
    
    def _process_timeout(self):
      time_now=now()
      for time,callback in self._timeout_events.iteritems():
        if time<time_now:
          callback()
          del self._timeout_events[time]
  ```