document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#compose-form').addEventListener('submit', submit_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {
  //clear out messages div if message had been loaded
  document.querySelector('#message-view').innerHTML = "";

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function submit_email (event) {
  event.preventDefault();
  //get values from form after submitting email
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
    })
  })
  .then(response => response.json())
  //redirect to sent mailbox after sending email
  .then(function() {
    load_mailbox('sent')
  })
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  //clear out messages div if message had been loaded
  document.querySelector('#message-view').innerHTML = "";

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;


    //fetch emails from api
    fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      for (let i = 0; i < emails.length; i++) {
        // take values from emails
        const id = emails[i]['id'];
        const sender = emails[i]['sender'];
        const recipients = emails[i]['recipients'];
        const subject = emails[i]['subject'];
        const time = emails[i]['timestamp'];
        const read = emails[i]['read'];
  
        // create div element (email listed in mailboxes)
        const email = document.createElement('div');
        email.classList.add("message");
        // add class if email has been read or email displayed in sent mailbox
        if (read || mailbox === 'sent') {
          email.classList.add("email-read");
        }
  
        // add click event handler to div (email)
        email.addEventListener('click', function() {
          viewEmail(id);
        });
        
        // render different values based on the mailbox
        if (mailbox === 'sent') {
          email.innerHTML = `<span>${recipients}</span> <span>${subject}</span> <span>${time}</span>`;
        } else {  
          email.innerHTML = `<span>${sender}</span> <span>${subject}</span> <span>${time}</span>`;
        }
  
        // append email
        document.querySelector('#emails-view').append(email);
      }  
    });
  }
  
  function viewEmail(id) {
    fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {
      // extract values from object in email [array]
      const sender = email['sender'];
      const recipients = email['recipients'];
      const subject = email['subject'];
      const time = email['timestamp'];
      const body = email['body'];
      const archived = email['archived'];
  
      // create archive and reply buttons.(if not in sent mailbox)
      const archiveButton = document.createElement("button");
      const replyButton = document.createElement("button");
      replyButton.innerHTML = "Reply";
      archiveButton.classList.add('btn', 'btn-light', 'btn-sm');
      replyButton.classList.add('btn', 'btn-light', 'btn-sm');
      if (archived === false) {
        archiveButton.innerHTML = "Archive";
      } else {
        archiveButton.innerHTML = "Unarchive";
      }
      
      archiveButton.addEventListener('click', function() {
        archiveEmail(id, archived);
      });
  
      replyButton.addEventListener('click', function() {
        replyEmail(email);
      });
  
      // get div element and populate with values of email
      const message = document.querySelector('#message-view');
      message.innerHTML = `<p><span class="m">To:</span> ${recipients}</p> <p><span class="m">From:</span> ${sender}</p> <p><span class="m">Subject:</span> ${subject}</p> <p><span class="m">Time:</span> ${time}<p> <p id="body">${body}</p>`;
  
      // display button if not in sent mailbox
      const userEmail = document.querySelector('h2').innerHTML;
      if (userEmail != sender) {
        message.prepend(archiveButton, " ", replyButton);
      }
    });
  
    //mark the email as read using a put request
    fetch(`/emails/${id}`, {
      method: 'PUT',
      body: JSON.stringify({
        read: true
      })
    })
    // Show message view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#message-view').style.display = 'block';
  }
  
  function archiveEmail (id, archived) {
    if (archived === false) {
      fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
          archived: true
        })
      })
      .then(function() {
        load_mailbox('inbox')
      })
    } else {
      fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
          archived: false
        })
      })
      .then(function() {
        load_mailbox('inbox')
      })
    }
  }
  
  function replyEmail(email) {
    compose_email();
    // Populate inputs with email info
    document.querySelector('#compose-recipients').value = email['sender'];
    // only add re: once in subject line
    if (email['subject'].startsWith('Re:')) {
      document.querySelector('#compose-subject').value = email['subject'];
    } else {
      document.querySelector('#compose-subject').value = `Re: ${email['subject']}`;
    }
    // add original email to form
    document.querySelector('#compose-body').value = `On ${email['timestamp']}, ${email['sender']} wrote:
  ${email['body']}
    `;
  }


