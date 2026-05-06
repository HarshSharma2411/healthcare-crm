// Auto-dismiss flash messages after 4 seconds
document.addEventListener('DOMContentLoaded', function () {
  const messages = document.querySelectorAll('.message');
  messages.forEach(function (msg) {
    setTimeout(function () {
      msg.style.transition = 'opacity .4s ease';
      msg.style.opacity = '0';
      setTimeout(function () { msg.remove(); }, 400);
    }, 4000);
  });

  // Confirm before delete form submission
  document.querySelectorAll('.confirm-card form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      if (!confirm('Are you sure? This action cannot be undone.')) {
        e.preventDefault();
      }
    });
  });
});
