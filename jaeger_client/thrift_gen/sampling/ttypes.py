#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,tornado
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class SamplingStrategyType(object):
  PROBABILISTIC = 0
  RATE_LIMITING = 1

  _VALUES_TO_NAMES = {
    0: "PROBABILISTIC",
    1: "RATE_LIMITING",
  }

  _NAMES_TO_VALUES = {
    "PROBABILISTIC": 0,
    "RATE_LIMITING": 1,
  }


class ProbabilisticSamplingStrategy(object):
  """
  Attributes:
   - samplingRate
  """

  thrift_spec = (
    None, # 0
    (1, TType.DOUBLE, 'samplingRate', None, None, ), # 1
  )

  def __init__(self, samplingRate=None,):
    self.samplingRate = samplingRate

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.DOUBLE:
          self.samplingRate = iprot.readDouble()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ProbabilisticSamplingStrategy')
    if self.samplingRate is not None:
      oprot.writeFieldBegin('samplingRate', TType.DOUBLE, 1)
      oprot.writeDouble(self.samplingRate)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.samplingRate is None:
      raise TProtocol.TProtocolException(message='Required field samplingRate is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.samplingRate)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RateLimitingSamplingStrategy(object):
  """
  Attributes:
   - maxTracesPerSecond
  """

  thrift_spec = (
    None, # 0
    (1, TType.I16, 'maxTracesPerSecond', None, None, ), # 1
  )

  def __init__(self, maxTracesPerSecond=None,):
    self.maxTracesPerSecond = maxTracesPerSecond

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I16:
          self.maxTracesPerSecond = iprot.readI16()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RateLimitingSamplingStrategy')
    if self.maxTracesPerSecond is not None:
      oprot.writeFieldBegin('maxTracesPerSecond', TType.I16, 1)
      oprot.writeI16(self.maxTracesPerSecond)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.maxTracesPerSecond is None:
      raise TProtocol.TProtocolException(message='Required field maxTracesPerSecond is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.maxTracesPerSecond)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class OperationSamplingStrategy(object):
  """
  Attributes:
   - operation
   - probabilisticSampling
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'operation', None, None, ), # 1
    (2, TType.STRUCT, 'probabilisticSampling', (ProbabilisticSamplingStrategy, ProbabilisticSamplingStrategy.thrift_spec), None, ), # 2
  )

  def __init__(self, operation=None, probabilisticSampling=None,):
    self.operation = operation
    self.probabilisticSampling = probabilisticSampling

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.operation = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.probabilisticSampling = ProbabilisticSamplingStrategy()
          self.probabilisticSampling.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('OperationSamplingStrategy')
    if self.operation is not None:
      oprot.writeFieldBegin('operation', TType.STRING, 1)
      oprot.writeString(self.operation)
      oprot.writeFieldEnd()
    if self.probabilisticSampling is not None:
      oprot.writeFieldBegin('probabilisticSampling', TType.STRUCT, 2)
      self.probabilisticSampling.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.operation is None:
      raise TProtocol.TProtocolException(message='Required field operation is unset!')
    if self.probabilisticSampling is None:
      raise TProtocol.TProtocolException(message='Required field probabilisticSampling is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.operation)
    value = (value * 31) ^ hash(self.probabilisticSampling)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class PerOperationSamplingStrategies(object):
  """
  Attributes:
   - defaultSamplingProbability
   - defaultLowerBoundTracesPerSecond
   - perOperationStrategies
  """

  thrift_spec = (
    None, # 0
    (1, TType.DOUBLE, 'defaultSamplingProbability', None, None, ), # 1
    (2, TType.DOUBLE, 'defaultLowerBoundTracesPerSecond', None, None, ), # 2
    (3, TType.LIST, 'perOperationStrategies', (TType.STRUCT,(OperationSamplingStrategy, OperationSamplingStrategy.thrift_spec)), None, ), # 3
  )

  def __init__(self, defaultSamplingProbability=None, defaultLowerBoundTracesPerSecond=None, perOperationStrategies=None,):
    self.defaultSamplingProbability = defaultSamplingProbability
    self.defaultLowerBoundTracesPerSecond = defaultLowerBoundTracesPerSecond
    self.perOperationStrategies = perOperationStrategies

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.DOUBLE:
          self.defaultSamplingProbability = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.DOUBLE:
          self.defaultLowerBoundTracesPerSecond = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.perOperationStrategies = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = OperationSamplingStrategy()
            _elem5.read(iprot)
            self.perOperationStrategies.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('PerOperationSamplingStrategies')
    if self.defaultSamplingProbability is not None:
      oprot.writeFieldBegin('defaultSamplingProbability', TType.DOUBLE, 1)
      oprot.writeDouble(self.defaultSamplingProbability)
      oprot.writeFieldEnd()
    if self.defaultLowerBoundTracesPerSecond is not None:
      oprot.writeFieldBegin('defaultLowerBoundTracesPerSecond', TType.DOUBLE, 2)
      oprot.writeDouble(self.defaultLowerBoundTracesPerSecond)
      oprot.writeFieldEnd()
    if self.perOperationStrategies is not None:
      oprot.writeFieldBegin('perOperationStrategies', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.perOperationStrategies))
      for iter6 in self.perOperationStrategies:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.defaultSamplingProbability is None:
      raise TProtocol.TProtocolException(message='Required field defaultSamplingProbability is unset!')
    if self.defaultLowerBoundTracesPerSecond is None:
      raise TProtocol.TProtocolException(message='Required field defaultLowerBoundTracesPerSecond is unset!')
    if self.perOperationStrategies is None:
      raise TProtocol.TProtocolException(message='Required field perOperationStrategies is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.defaultSamplingProbability)
    value = (value * 31) ^ hash(self.defaultLowerBoundTracesPerSecond)
    value = (value * 31) ^ hash(self.perOperationStrategies)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SamplingStrategyResponse(object):
  """
  Attributes:
   - strategyType
   - probabilisticSampling
   - rateLimitingSampling
   - operationSampling
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'strategyType', None, None, ), # 1
    (2, TType.STRUCT, 'probabilisticSampling', (ProbabilisticSamplingStrategy, ProbabilisticSamplingStrategy.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'rateLimitingSampling', (RateLimitingSamplingStrategy, RateLimitingSamplingStrategy.thrift_spec), None, ), # 3
    (4, TType.STRUCT, 'operationSampling', (PerOperationSamplingStrategies, PerOperationSamplingStrategies.thrift_spec), None, ), # 4
  )

  def __init__(self, strategyType=None, probabilisticSampling=None, rateLimitingSampling=None, operationSampling=None,):
    self.strategyType = strategyType
    self.probabilisticSampling = probabilisticSampling
    self.rateLimitingSampling = rateLimitingSampling
    self.operationSampling = operationSampling

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.strategyType = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.probabilisticSampling = ProbabilisticSamplingStrategy()
          self.probabilisticSampling.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.rateLimitingSampling = RateLimitingSamplingStrategy()
          self.rateLimitingSampling.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.operationSampling = PerOperationSamplingStrategies()
          self.operationSampling.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SamplingStrategyResponse')
    if self.strategyType is not None:
      oprot.writeFieldBegin('strategyType', TType.I32, 1)
      oprot.writeI32(self.strategyType)
      oprot.writeFieldEnd()
    if self.probabilisticSampling is not None:
      oprot.writeFieldBegin('probabilisticSampling', TType.STRUCT, 2)
      self.probabilisticSampling.write(oprot)
      oprot.writeFieldEnd()
    if self.rateLimitingSampling is not None:
      oprot.writeFieldBegin('rateLimitingSampling', TType.STRUCT, 3)
      self.rateLimitingSampling.write(oprot)
      oprot.writeFieldEnd()
    if self.operationSampling is not None:
      oprot.writeFieldBegin('operationSampling', TType.STRUCT, 4)
      self.operationSampling.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.strategyType is None:
      raise TProtocol.TProtocolException(message='Required field strategyType is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.strategyType)
    value = (value * 31) ^ hash(self.probabilisticSampling)
    value = (value * 31) ^ hash(self.rateLimitingSampling)
    value = (value * 31) ^ hash(self.operationSampling)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
