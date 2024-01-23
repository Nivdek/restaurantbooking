django.jQuery.ajaxSetup({
    beforeSend: function (xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", '{% csrf_token %}');
    }
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
            // Extract the tab identifier from the hash
            var tabIdentifier = hash.replace('#nav-', '');

            // Update the URL dynamically
            var tabUrl = '/accountpage/accountoverview/?tab=' + tabIdentifier;

            // Use Bootstrap's Tab JavaScript methods to activate the tab
            var tabSelector = 'button[data-bs-target="' + hash + '"]';
            var tab = $(tabSelector)[0];
            if (tab) {
                var tabPaneId = $(tab).attr('data-bs-target');
                var tabContentId = $(tabPaneId).attr('id');
                
                // Load content dynamically using AJAX
                console.log(tabUrl);
                $.ajax({
                    url: tabUrl,  // Use the dynamically constructed URL
                    type: 'GET',
                    success: function (data) {
                        console.log(data);
                        // Update the content of the tab pane
                        $('#' + tabContentId).html(data);
                    },
                    error: function (error) {
                        console.log(error);
                    }
                });

                var tabInstance = new bootstrap.Tab(tab);
                tabInstance.show();
                $('#' + tabContentId).addClass('show active');
            }
        } else if (window.location.pathname.includes('accountoverview')) {
            // If no hash is present and on the accountoverview page, activate the default tab and append the hash
            var defaultTab = '#nav-profile-tab';
            var defaultTabPaneId = $(defaultTab).attr('data-bs-target');
            var defaultTabContentId = $(defaultTabPaneId).attr('id');
            var defaultTabInstance = new bootstrap.Tab(defaultTab);
            defaultTabInstance.show();
            $('#' + defaultTabContentId).addClass('show active');

            // Append the hash to the URL
            window.location.hash = defaultTabPaneId.replace('#nav-', '#');
        }
    }

     // Listen for changes in the URL hash
     $(window).on('hashchange', activateTabFromHash);

     // Activate the initial tab based on the URL hash
     activateTabFromHash();
 
     // Trigger hashchange event after activating the initial tab
     $(window).trigger('hashchange');
 });