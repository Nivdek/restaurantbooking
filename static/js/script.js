/* Script for the DateTimeField in the BookingForm */
django.jQuery(document).ready(function ($) {
    $('.datetimepicker-input').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss',  // Specify the desired date and time format
    });
});

/* Script for URL Hashing in the accountoverview */
django.jQuery(document).ready(function ($) {
  // Function to update the URL hash when a tab is clicked
  $('.nav-link').on('click', function () {
      var tabId = $(this).attr('data-bs-target');
      window.location.hash = tabId.replace('#nav-', '#');
  });

  // Function to activate the tab based on the URL hash
  function activateTabFromHash() {
      var hash = window.location.hash;
      if (hash) {
          // Use Bootstrap's Tab JavaScript methods to activate the tab
          var tabSelector = 'button[data-bs-target="' + hash + '"]';
          var tab = $(tabSelector)[0];
          if (tab) {
              var tabPaneId = $(tab).attr('data-bs-target');
              var tabContentId = $(tabPaneId).attr('id');
              var tabInstance = new bootstrap.Tab(tab);
              tabInstance.show();
              $('#' + tabContentId).addClass('show active');
          }
      }
  }

  // Listen for changes in the URL hash
  $(window).on('hashchange', activateTabFromHash);

  // Activate the initial tab based on the URL hash
  activateTabFromHash();
});


  