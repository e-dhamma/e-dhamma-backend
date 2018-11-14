export default (value) => {
  const date = new Date(value)
  return date.toLocaleString('et-ee', {day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit'})
}
